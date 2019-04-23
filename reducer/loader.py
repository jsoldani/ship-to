from shutil import copyfile
import errno
import os
import sys

# function for loading files needed by "reducer.pl" in "config" folder
def loadReducerConfig(topologyPl,reducerPath):
    # create "config" folder (if not existing yet)
    try:
        os.mkdir("config")
    except Exception as e:
        if e.errno != errno.EEXIST:
            print(e)

    # load files in "config" folder
    targetTopologyPl = reducerPath + "/config/topology.pl"
    copyfile(topologyPl,targetTopologyPl)

def main(args):
    # check command line arguments
    if(len(args) < 1):
        print("usage: loader.py <topologyFile.pl>")
        exit(2)

    loadReducerConfig(args[0],".")

main(sys.argv[1:])
