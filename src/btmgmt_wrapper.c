/*
 *  Copyright (C) 2020 James Bennion-Pedley. All rights reserved.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
 *
 */

/*
    This file contains the main Python wrapper for the btmgmt interface:
    new library features should be implemented here.
*/

#include <stdio.h>
#include <unistd.h>
#include <Python.h>

/*
    Include C source for the btmgmt interface: as heinous as this looks, it
    makes a lot of sense here, as all the functions in btmgmt.c are static,
    and we want to put a very small wrapper around these functions. This way,
    the original source file can be used, so any changes will update with the
    rest of the submodule.
*/

#include "tools/btmgmt.c"

static PyObject * btmgmt_command(PyObject *self, PyObject *args)
{
	// Loop through the input argument and pass pointers to argv[]
	Py_ssize_t args_len = PyTuple_Size(args);
	char *argv[args_len + 1];
	argv[0] = "btmgmt";
	for (uint8_t i = 0; i < args_len; i++) {
		argv[i + 1] = PyUnicode_DATA(PyTuple_GetItem(args, i));
	}
	int argc = args_len + 1;

	// Open management shell and pass function arguments as parameters
	int status = 0;
	bt_shell_init(argc, argv, &opt);
	bt_shell_set_menu(&main_menu);

	// Create HCI management socket
	mgmt = mgmt_new_default();
	if (!mgmt) {
		fprintf(stderr, "Unable to open mgmt_socket!\n");
		return PyLong_FromLong(EXIT_FAILURE);
	}

	if (getenv("MGMT_DEBUG"))
		mgmt_set_debug(mgmt, mgmt_debug, "mgmt: ", NULL);

	if (index_option)
		set_index(index_option);

	register_mgmt_callbacks(mgmt, mgmt_index);

	// Execute Command
	bt_shell_attach(fileno(stdin));
	update_prompt(mgmt_index);
	status = bt_shell_run();

	// Cleanup
	mgmt_cancel_all(mgmt);
	mgmt_unregister_all(mgmt);
	mgmt_unref(mgmt);

	return PyLong_FromLong(status);
}

static PyObject * btmgmt_command_str(PyObject *self, PyObject *args)
{
	char* buf;
	size_t buf_len;
	int buf_pipe[2];

	// Backup stdout/stderr and flush buffer
	int stdout_copy = dup(STDOUT_FILENO);
	int stderr_copy = dup(STDERR_FILENO);
	fflush(stdout);
	fflush(stderr);

	// Redirect stdout/stderr to pipe
	if(pipe(buf_pipe) != 0) {
		exit(1);
	}
	
	dup2(buf_pipe[1], STDOUT_FILENO);
	dup2(buf_pipe[1], STDERR_FILENO);
	close(buf_pipe[1]);

	// Call underlying btmgmt command function
	PyObject* status = btmgmt_command(self, args);
	
	// Return stdout/stderr to original descriptor
	fflush(stdout);
	fflush(stderr);
	dup2(stdout_copy, STDOUT_FILENO);
	dup2(stderr_copy, STDERR_FILENO);
	close(stdout_copy);
	close(stderr_copy);

	// Copy data to memstream and close read-end of pipe
	FILE* mem_stdout = open_memstream(&buf, &buf_len);
	FILE* pipe_stdout = fdopen(buf_pipe[0], "r");

	int c;
	while((c = fgetc(pipe_stdout)) != EOF) {
		fputc(c, mem_stdout);
	}
	fclose(mem_stdout);
	fclose(pipe_stdout);

	// Build returned tuple and free memstream
	PyObject* str = PyUnicode_FromStringAndSize(buf, buf_len);
	free(buf);

	return PyTuple_Pack(2, status, str);
}

static PyMethodDef btmgmt_methods[] = {
	{"command", (PyCFunction)btmgmt_command, METH_VARARGS, "mgmt-api command"},
	{"command_str", (PyCFunction)btmgmt_command_str, METH_VARARGS, "mgmt-api command with returned string"},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef btmgmt_definition = { 
	PyModuleDef_HEAD_INIT,
	"btmgmt",
	"A Python wrapper for interfacing with the btmgmt API for BlueZ under Linux",
	-1, 
	btmgmt_methods
};

PyMODINIT_FUNC PyInit_btmgmt(void)
{
	Py_Initialize();
	return PyModule_Create(&btmgmt_definition);
}
