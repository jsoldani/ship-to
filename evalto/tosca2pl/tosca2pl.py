import errno
import os
import sys
from toscaparser.tosca_template import ToscaTemplate

# function to typeset "node(name,type,cost)" and output it on a given file
def writeNodeOnFile(file, node):
    nodeName = node[0]
    nodeType = node[1]
    file.write("node(" + nodeName + "," + nodeType + ",c_" + nodeName + ").\n")

# function to typeset "edge(direction,source,target)" and output it on a given file
def writeRelationshipOnFile(file,relationship,direction):
    source = relationship[0]
    target = relationship[1]
    file.write("edge(" + direction + "," + source + "," + target + ").\n")

# function to parse a tosca "inputFile" and output its representation in prolog
def parse(inputFile,outputFile):
    # parse TOSCA file
    app = ToscaTemplate(inputFile,None,True)

    # retrieve nodes and relationships
    nodes = []
    hRels = []
    vRels = []
    for n in app.nodetemplates:
        # get current node - represented as [name, type]
        node = []
        nodeName = n.name.replace("-","_")
        node.append(nodeName)
        nodeTypeTokens = n.type.split(".")
        nodeType = nodeTypeTokens[0]
        for i in range(1,len(nodeTypeTokens)):
            token = nodeTypeTokens[i]
            upperToken = "" + token[0].upper()
            upperToken = upperToken + token[1:]
            nodeType = nodeType + upperToken
        node.append(nodeType)
        nodes.append(node)

        for requirementMap in n.requirements:
            # get current relationship - represented as [source, target]
            relationship = []
            for requirementName in requirementMap.keys():
                # get relationship's source
                relationship.append(n.name)
                # get relationship's target
                requirement = requirementMap.get(requirementName)
                try:
                        relationship.append(requirement.get("node"))
                except AttributeError:
                        relationship.append(requirement)
                # classify relationship as vertical or horizontal
                if requirementName == "host":
                    vRels.append(relationship)
                else:
                    hRels.append(relationship)

    # adds bottom node (if needed)
    bottomNodes = []

    for node in nodes:
        nodeName = node[0]
        isBottom = True
        for vRel in vRels:
            source = vRel[0]
            if source == nodeName:
                isBottom = False
        if isBottom:
            bottomNodes.append(node)

    if len(bottomNodes) > 1:
        bottom = ["bottom","bottom"]
        nodes.append(bottom)
        for node in bottomNodes:
            relToBottom = []
            relToBottom.append(node[0])
            relToBottom.append("bottom")
            vRels.append(relToBottom)

    # create "output" folder (if not existing yet)
    try:
        os.mkdir("output")
    except Exception as e:
        if e.errno != errno.EEXIST:
            print(e)

    # output nodes and relationship on file
    outputFileWithFolder = "output/" + outputFile
    output = open(outputFileWithFolder,"w")

    for node in nodes:
        writeNodeOnFile(output,node)

    output.write("\n")

    for hRel in hRels:
        writeRelationshipOnFile(output,hRel,"h")

    output.write("\n")

    for vRel in vRels:
        writeRelationshipOnFile(output,vRel,"v")

    output.close()

# main function
def main(args):
    if len(args) < 2:
        print("usage: parser.py <inputFile> <outputFile>")
        sys.exit(2)

    inputFile = args[0]
    outputFile = args[1]
    parse(inputFile,outputFile)

# run main function
main(sys.argv[1:])
