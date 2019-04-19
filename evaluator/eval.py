import sys

# function reading and returning the term in inputFile
def getTerm(inputFile):
    file = open(inputFile,"r")
    term = file.readline()
    return term

# main function
def main(args):
    # parse command line arguments
    if len(args) < 1:
        print("usage: parser.py <inputFile>")
        sys.exit(2)
    inputFile = args[0]

    # get term to be evaluated
    term = getTerm(inputFile)

    # temp - output term
    print(term)

# run main function
main(sys.argv[1:])
