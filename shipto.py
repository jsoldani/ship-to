import os
import sys

def main(args):
    # check and parse command line arguments
    if len(args) < 3:
        print("usage: shipto.py <toscaFile> <costsFile.py> <edgeNodesFile.py>")
        exit(2)
    toscaFile = os.path.abspath(args[0])
    costsFile = os.path.abspath(args[1])
    edgeNodesFile = os.path.abspath(args[2])

	# configuring desired evalto instance
    print("Configuring solver...", end="")
    # TODO implement environment configuration
    print("done!")

	# launching evalto topology from TOSCA to prolog
    print("Finding feasible application deployments...", end="")
    out = os.system("python evalto\evalto.py " + toscaFile + " " + costsFile + " " + edgeNodesFile)
    print("done!")

    # print result
    print("** Identified feasible application deployments **")
	# TODO printout results

main(sys.argv[1:])
