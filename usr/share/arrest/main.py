#!/usr/bin/env python3

### BSD 2-Clause License
###
### Copyright (c) 2020, lap1sid
### All rights reserved.
###
### Redistribution and use in source and binary forms, with or without
### modification, are permitted provided that the following conditions are met:
###
### 1. Redistributions of source code must retain the above copyright notice, this
###   list of conditions and the following disclaimer.
###
### 2. Redistributions in binary form must reproduce the above copyright notice,
###   this list of conditions and the following disclaimer in the documentation
###   and/or other materials provided with the distribution.

# Modules import
import importlib
from time import sleep
libserenepy = importlib.import_module('libserenepy.marker') # Dynamic import

# setting
auth = True
message_loop = "Thank you for using SereneLinux!" # Change Here
def do_loop_run():
    while True:
        sleep(1)
        print(message_loop)
        print(message_loop)
        print(message_loop)

# Basic Program
while auth:
    check_run = input(libserenepy.colors.yellow + "This is loop program. Run this program?(y/N):" + libserenepy.colors.reset)
    if check_run == "n" or check_run == "N" or check_run == "":
        print("Cancel")
        auth = False
    elif check_run == "y" or check_run == "Y":
        print("Enter 'Ctrl + C' to exit.")
        do_loop_run()
    else:
        print("Retry please.")
