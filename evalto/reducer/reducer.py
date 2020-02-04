import os
import errno
import sys
from pyswip import Prolog

# function for reducing a topology to a term "l(type,dir,term1,term2)"
def reduce(outputFile):
    # load Prolog program "reducer"
    prolog = Prolog()
    prolog.consult("prolog/reducer.pl")

    # check well-formedness
    violating = list(prolog.query("violatingWellFormedness(L1,L2)"))
    violating1 = violating[0]["L1"]
    violating2 = violating[0]["L2"]
    if len(violating1) > 0 or len(violating2) > 0:
        # print violations (if any)
        print("ERROR: topology is not well-formed because")
        for n in violating1:
            print("- node " + str(n) + " violates condition (i) of well-formedness")
        for n in violating2:
            print("- node " + str(n) + " violates condition (ii) of well-formedness")
        exit(2)

    # compute first possible solution (if any)
    results = list(prolog.query("loop(R)", maxresult=1))
    if len(results) > 0:
        # if solvable, save first result
        result = results[0]["R"]
    else:
        # otherwise, return error message for non well-formed topology
        print("ERROR: something went wrong...is topology rooted?")
        exit(2)

    # create "output" folder (if not existing yet)
    try:
        os.mkdir("output")
    except Exception as e:
        if e.errno != errno.EEXIST:
            print(e)

    # output term on "outputFile"
    outputFileWithFolder = "output/" + outputFile
    output = open(outputFileWithFolder,"w")
    output.write(result)

def main(args):
    # check command line arguments
    if len(args) < 1:
        print("usage: reducer.py <outputFile>")
        exit(2)
    # reduce topology and output on file
    reduce(args[0])

main(sys.argv[1:])
