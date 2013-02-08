#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013
#
# Marcelo Barbosa <mr.marcelo.barbosa@gmail.com>
# Special thanks for Alisson Ramos de Oliveira <a2r7o6@gmail.com>,
# initial author script.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import sys
import urllib2
import simplejson as json


zabbix_api = 'YOUR_URL_ZABBIX_HERE/api_jsonrpc.php'
username = "USERNAME_PRIVILEGES_API_ACCESS"
password = "PASSWORD"


def get_auth(username, password):
    """
    Request authentication via JSON to Zabbix API
    """
    req = get_json_data({
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": username,
            "password": password
        },
        "id": 0
    })
    if 'result' in req:
        return req['result']
    else:
        print "ZABBIX API AUTHENTICATION FAILED"
        sys.exit()


def get_json_data(data):
    """
    GetJsonData any request JSON from Zabbix API
    """
    json_object = json.dumps(data)
    req = urllib2.Request(zabbix_api, json_object)
    req.add_header("Content-Type", "application/json-rpc")
    try:
        response = urllib2.urlopen(req)
    except:
        print "ZABBIX API IT\'S NOT ACCESS"
        sys.exit()
    reads = response.read()
    json_object = json.loads(reads)
    return json_object
