import sys

# function reading and returning the term in inputFile
def getTerm(inputFile):
    file = open(inputFile,"r")
    term = file.readline().replace(" ","").replace("l","")
    return term

# function for parsing terms "l(nodeType,direction,subTerm1,subTerm2)"
def parseTerm(termTxt):
    termDict = {}

    # remove outer parentheses
    parametersTxt = termTxt[1:-1]

    # get node type
    firstComma = parametersTxt.find(",")
    termDict["type"] = parametersTxt[:firstComma]
    parametersTxt = parametersTxt[firstComma+1:]

    # get direction
    secondComma = parametersTxt.find(",")
    termDict["dir"] = parametersTxt[:secondComma]
    parametersTxt = parametersTxt[secondComma+1:]

    # get subTerm1
    if parametersTxt[0] == '(':
        # if the term is itself parenthesised, identify the index "i" where it
        # ends by counting "opened" and "closed" parentheses
        opened = 1 # opened parentheses
        closed = 0 # closed parentheses
        i = 1 # index for traversing subTerm1
        while closed < opened:
            if parametersTxt[i] == '(':
                opened = opened + 1
            if parametersTxt[i] == ')':
                closed = closed + 1
            i = i + 1
        # then, parse the subterm recursively
        termDict["term1"] = parseTerm(parametersTxt[:i])
        parametersTxt = parametersTxt[i+1:]
    else:
        # otherwise, get string until next comma
        thirdComma = parametersTxt.find(",")
        termDict["term1"] = parametersTxt[:thirdComma]
        parametersTxt = parametersTxt[thirdComma+1:]

    # get subTerm2
    if parametersTxt[0] == '(':
        # if the term is parenthesised, parse it recursively
        termDict["term2"] = parseTerm(parametersTxt)
    else:
        # otherwise simply take it as string
        termDict["term2"] = parametersTxt
    return termDict

# (debugging) function for printing the dictionary representing a term
def printTerm(term,nesting):
    if type(term) is dict:
        print("\t"*nesting, "type: ", term["type"])
        print("\t"*nesting, "dir: ", term["dir"])
        print("\t"*nesting, "term1:")
        printTerm(term["term1"],nesting+1)
        print("\t"*nesting, "term2:")
        printTerm(term["term2"],nesting+1)
    else:
        print("\t"*nesting, term)

# main function
def main(args):
    # parse command line arguments
    if len(args) < 1:
        print("usage: parser.py <inputFile>")
        sys.exit(2)
    inputFile = args[0]

    # get term to be evaluated
    termTxt = getTerm(inputFile)
    term = parseTerm(termTxt)

    printTerm(term,0) # debugging

    # TODO - input python description of costs and compositors
    # (see https://stackoverflow.com/questions/26062994/how-can-i-import-a-python-file-through-a-command-prompt)
    # TODO - evaluate parsed term to get output value

# run main function
main(sys.argv[1:])
