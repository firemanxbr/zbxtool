#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013
#
# Marcelo Barbosa <mr.marcelo.barbosa@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import time
import datetime


def timestamp_to_date(timestamp):
    """
    Convert timestamp to date format %Y-%m-%d %H:%M:%S
    """
    date = (datetime.datetime.fromtimestamp(
        int(timestamp)).strftime('%Y-%m-%d %H:%M:%S'))

    return date


def date_to_timestamp(date):
    """
    Convert date format %Y-%m-%d %H:%M:%S to timestamp integer
    """
    timestamp = int(time.mktime(time.strptime(date, '%Y-%m-%d %H:%M:%S')))

    return timestamp
