from toscaparser.tosca_template import ToscaTemplate

def writeNodeOnFile(file, node):
    nodeName = node[0]
    nodeType = node[1]
    file.write("node(" + nodeName + "," + nodeType + ",c_" + nodeName + ").\n")

def writeRelationshipOnFile(file,relationship,direction):
    source = relationship[0]
    target = relationship[1]
    file.write("edge(" + direction + "," + source + "," + target + ").\n")

# parse TOSCA file
appPath = "data/examples/thinking.yml" # temporary - for development
app = ToscaTemplate(appPath,None,True)

# retrieve nodes and relationships
nodes = []
hRels = []
vRels = []
for n in app.nodetemplates:
    # get current node - represented as [name, type]
    node = []
    nodeName = n.name
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

# output nodes and relationship on file
outputFile = open("topology.pl","w")

for node in nodes:
    writeNodeOnFile(outputFile,node)

outputFile.write("\n")

for hRel in hRels:
    writeRelationshipOnFile(outputFile,hRel,"h")

outputFile.write("\n")

for vRel in vRels:
    writeRelationshipOnFile(outputFile,vRel,"v")

outputFile.close()