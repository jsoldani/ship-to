from shutil import copyfile
import errno
import os
import sys

def main(args):
    # check command line arguments
    if(len(args) < 2):
        print("usage: loader.py <compositorsFile.py> <costsFile.py>")
        exit(2)

    # copy files to set environment for "evaluator.py"
    try:
        os.mkdir("config")
    except Exception as e:
        if e.errno != errno.EEXIST:
            print(e)

    targetCompositors = "config/compositors.py"
    targetCosts = "config/costs.py"
    copyfile(args[0],targetCompositors)
    copyfile(args[1],targetCosts)


main(sys.argv[1:])
