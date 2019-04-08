#!/usr/bin/env python3
#Modules import
from color import colors
from time import sleep

#setting
auth = True
message_loop = "Change Here!"
def do_loop_run():
    while True:
        sleep(1)
        print(message_loop)
        print(message_loop)
        print(message_loop)

#Basic Program
while auth:
    check_run = input(colors.yellow + "This is loop program. Run this program?(y/N):" + colors.reset)
    if check_run == "n" or check_run == "N" or check_run == "":
        print("Cancel")
        auth = False
    elif check_run == "y" or check_run == "Y":
        print("Enter 'Ctrl + C' to exit.")
        do_loop_run()
    else:
        print("Retry please.")
