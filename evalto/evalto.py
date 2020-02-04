import os
import sys

def main(args):
    # check and parse command line arguments
    if len(args) < 3:
        print("usage: evalto.py <toscaFile> <compositorsFile.py> <costsFile.py>")
        exit(2)
    toscaFile = os.path.abspath(args[0])
    compositorsFile = os.path.abspath(args[1])
    costsFile = os.path.abspath(args[2])

	# setting running dir to "evalto" dir
    os.chdir("evalto")

    # translate topology from TOSCA to prolog
    print("Parsing TOSCA file...", end="")
    os.chdir("tosca2pl")
    os.system("python tosca2pl.py " + toscaFile + " topology.pl")
    topologyPl = os.getcwd() + "/output/topology.pl"
    print("done!")

    # reduce topology
    print("Reducing topology to evaluable term...", end="")
    os.chdir("../reducer")
    os.system("python loader.py " + topologyPl)
    os.system("python reducer.py " + "term.txt")
    termTxt = os.getcwd() + "/output/term.txt"
    print("done!")

    # evaluate topology
    print("Evaluating topology...", end="")
    os.chdir("../evaluator")
    os.system("python loader.py " + compositorsFile + " " + costsFile)
    os.system("python evaluator.py " + termTxt + " result.txt")
    print("done!")

	# restoring working dir
	os.chdir("..")

main(sys.argv[1:])
