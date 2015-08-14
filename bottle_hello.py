#!/usr/bin/python 
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2015, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# bottle_hello.py
# a simple example to build a http response using bottle
#
# Author : sosorry
# Date   : 08/01/2015

from bottle import *

@route('/')
def index():
    return "Hello Bottle"

if __name__ == "__main__":
    run(host='0.0.0.0', port=8080)

