#!/usr/bin/env python3
from sys import argv
from ErrorHandlers.ErrorHandler import throwError

def checkArgumentLine():
    nbArguments = len(argv)
    if nbArguments < 2 :
        throwError("CSV file expected in parameters.", 1, True)
    if nbArguments > 2 :
        throwError("Too much argument given in command line.", 2, True)
