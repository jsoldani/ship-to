from shutil import copyfile
import errno
import os
import sys

# function for loading files needed by "evaluator.py" in "config" folder
def loadEvaluatorConfig(compositorsPy,costsPy):
    # create "config" folder (if not existing yet)
    try:
        os.mkdir("config")
    except Exception as e:
        if e.errno != errno.EEXIST:
            print(e)

    # load files in "config" folder
    targetCompositors = "config/compositors.py"
    targetCosts = "config/costs.py"
    copyfile(compositorsPy,targetCompositors)
    copyfile(costsPy,targetCosts)

def main(args):
    # check command line arguments
    if(len(args) < 2):
        print("usage: loader.py <compositorsFile.py> <costsFile.py>")
        exit(2)

    # load files
    loadEvaluatorConfig(args[0],args[1])

main(sys.argv[1:])
