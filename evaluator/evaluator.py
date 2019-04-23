import sys
from config.costs import cost
from config.compositors import compositor

# function reading and returning the term in inputFile
def getTerm(inputFile):
    file = open(inputFile,"r")
    term = file.readline().replace(" ","").replace("l(","(")
    return term

# function for parsing terms "l(nodeType,direction,subTerm1,subTerm2)"
def parseTerm(termTxt):
    termDict = {}

    # remove outer parentheses
    afterOuterOpenedParenthesis = termTxt.find("(") + 1
    beforeOuterClosedParenthesis = termTxt.rfind(")")
    parametersTxt = termTxt[afterOuterOpenedParenthesis:beforeOuterClosedParenthesis]

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

# function evaluating a parsed term (dictionary, see 'parseTerm')
def evalTerm(term):
    if isinstance(term,str):
        node = term[2:]
        return cost(node)
    else:
        comp = compositor(term["type"],term["dir"])
        costTerm1 = evalTerm(term["term1"])
        costTerm2 = evalTerm(term["term2"])
        return comp(costTerm1,costTerm2)

def eval(inputFile):
    # get term to be evaluated
    termTxt = getTerm(inputFile)
    term = parseTerm(termTxt)
    # evaluate parsed term to get output value
    totalCost = evalTerm(term)
    return totalCost

# main function
def main(args):
    # parse command line arguments
    if len(args) < 1:
        print("usage: parser.py <inputFile>")
        sys.exit(2)
    inputFile = args[0]

    totalCost = eval(inputFile)
    print(totalCost)

# run main function
main(sys.argv[1:])
