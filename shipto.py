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
    # TODO generate needed python objects from costsFile and edgeNodesFile
    # TODO prepare examples, destroy "evalto" ones
    print("done!")

    # launching evalto topology from TOSCA to prolog
    print("Finding feasible application deployments...", end="")
    # TODO pass generated python objects to evalto
    out = os.system("python evalto\evalto.py " + toscaFile + " " + costsFile + " " + edgeNodesFile)
    print("done!")

    # printing results
    print("** Identified feasible application deployments **")
    resultTxt = os.getcwd() + "/evalto/output.txt"
    resultFile = open(resultTxt)
    print(resultFile.read())
    resultFile.close()

main(sys.argv[1:])
