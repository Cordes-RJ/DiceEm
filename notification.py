# -*- coding: utf-8 -*-

import sys

# Messages
msgEnd = "\n-------------------------------------------\n"

# checkBeforeContinuing allows the user to decide whether or not to continue
def checkBeforeContinuing(msg):
    print(msg + "\n")
    if input("Would you like to continue?\ny/n:") == "y":
        print("Continuing..." + msgEnd)
    else:
        close("User chose to stop the emulator")

# close notifies the user and closes the program
def close(msg):
    print("\n" + msg)
    print("\nClosing...\n")
    sys.exit()