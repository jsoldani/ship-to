import os
import json
import sys
import yaml

def main(args):
    # check and parse command line arguments
    if len(args) < 2:
        print("usage: shipto.py <toscaFile> <deploymentInfoFile>")
        exit(2)
    toscaFile = os.path.abspath(args[0])
    deploymentInfoFile = os.path.abspath(args[1])

    # configuring desired evalto instance
    print("Configuring solver...", end="")
    targetFolder = os.getcwd() + "/tmp"
    out = os.system("python loader/loader.py " + toscaFile + " " + deploymentInfoFile + " " + targetFolder)
    print("done!")

    # launching evalto topology from TOSCA to prolog
    compsFilePath = targetFolder + "/compositors.py"
    costsFilePath = targetFolder + "/costs.py"
    out = os.system("python evalto/evalto.py " + toscaFile + " " + compsFilePath + " " + costsFilePath)

    # generating YAML file from evalto output
    evaltoOutput = os.getcwd() + "/evalto/output.txt"
    targetYaml = "placement.yml"
    out = os.system("python exporter/exporter.py " + evaltoOutput + " " + targetYaml)
    print("|\n|--> Results placed in ", targetYaml)

main(sys.argv[1:])
