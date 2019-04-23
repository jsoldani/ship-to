from shutil import copyfile
import sys

def main(args):
    # check command line arguments
    if(len(args) < 1):
        print("usage: loader.py <topologyFile.pl>")
        exit(2)

    copyfile(args[0],"topology.pl")

main(sys.argv[1:])
