import os
import errno
import sys
from pyswip import Prolog

# function for reducing a topology to a term "l(type,dir,term1,term2)"
def reduce(outputFile):
    # load Prolog program "reducer"
    prolog = Prolog()
    prolog.consult("prolog/reducer.pl")
    # compute all possible, equivalent reductions (and save first)
    results = list(prolog.query("loop(R)"))
    result = results[0]["R"]

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
