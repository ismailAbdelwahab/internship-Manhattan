#!/usr/bin/env python3
from sys import argv, exit

####################### Error Handling ##############################
def throwError( error_message, exit_code=1, print_proper_usage=False):
    print("  **Error: " + error_message )
    if print_proper_usage :
        properUsage()
    exit( exit_code )

####################### Proper Usage ################################
def properUsage():
    print(" Proper usage: "+ argv[0] + " file.csv")
    print("  <file.csv> should contain your points:")
    print("    1) One point per line.")
    print("    2) x then y values separated with a comma.")
