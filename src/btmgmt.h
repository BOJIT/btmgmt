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
    This file contains declarations of all the functions we want to use from
    btmgmt.c: it is not automatically updated when there are upstream changes
    to the BlueZ submodule, so is maintained as part of the Python wrapper.
*/

#include <stdlib.h>

#include "src/shared/mgmt.h"
#include "src/shared/shell.h"

static struct mgmt *mgmt;

static uint16_t mgmt_index;

static const struct bt_shell_opt opt;

static const struct bt_shell_menu main_menu;

static const char *index_option;

static void mgmt_debug(const char *str, void *user_data);

static void set_index(const char *arg);

static void register_mgmt_callbacks(struct mgmt *mgmt, uint16_t index);

static void update_prompt(uint16_t index);
