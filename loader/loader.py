import json
import os
import sys
import yaml

def parseYaml(file):
    yFile = open(file)
    yml = yaml.load(yFile, Loader=yaml.FullLoader)
    yFile.close()
    return yml

def generateCosts(tosca, deploymentInfo):
    # creating empty costs dictionary
    costs = {}

    # adding cost for bottom
    costs["bottom"] = []

    # filling costs with node costs
    nodeTemplates = tosca["topology_template"]["node_templates"]
    for nodeName in nodeTemplates:
        nodeTemplate = nodeTemplates[nodeName]
        if "Compute" in nodeTemplate["type"]:
            cost = {}
            cost["name"] = nodeName
            cost["memory"] = 0
            cost["storage"] = 0
            cost["clusterNodes"] = deploymentInfo["clusterNodes"]
            costs[nodeName] = [cost]
        else:
            costs[nodeName] = deploymentInfo["consumption"][nodeName]

    # returning generated costs
    return costs

def generateCostsPy(costs,costsFilePath):
    costsFile = open(costsFilePath, "w+")

    costsFile.write("costs = " + json.dumps(costs))

    costsGetterPy = open("config/costs-template-getter.py")
    costsFile.write("\n")
    costsFile.write(costsGetterPy.read())
    costsGetterPy.close()

    costsFile.close()


def generateCompositors(tosca, deploymentInfo):
    # creating empty comps dictionary for compositors
    comps = {}

    # adding compositors for bottom
    comps["bottom"] = {}
    comps["bottom"]["h"] = "union_placements"
    comps["bottom"]["v"] = "union_placements"

    # filling comps with functions for solving feasible placement problem
    nodeTemplates = tosca["topology_template"]["node_templates"]
    for nodeName in nodeTemplates:
        nodeType = nodeTemplates[nodeName]["type"]
        if not(nodeType in comps):
            if "Compute" in nodeType:
                comps[nodeType] = {}
                comps[nodeType]["h"] = "sum_consumptions"
                comps[nodeType]["v"] = "update_placement"
            else:
                comps[nodeType] = {}
                comps[nodeType]["h"] = "sum_consumptions"
                comps[nodeType]["v"] = "sum_consumptions"

    # returning generated costs
    return comps

def generateCompositorsPy(comps,compsFilePath):
    compsFile = open(compsFilePath, "w+")

    compsFunctionsPy = open("config/compositors-template-functions.py")
    compsFile.write(compsFunctionsPy.read())
    compsFunctionsPy.close()

    compsFile.write("compositors = { ") # + json.dumps(comps))
    for nodeType in comps:
        compsFile.write(" '" + nodeType.replace(".","").lower() + "': {")
        compsFile.write(" 'h': " + comps[nodeType]["h"] + ",")
        compsFile.write(" 'v': " + comps[nodeType]["v"])
        compsFile.write("}, ")
    compsFile.write(" }")

    compsGetterPy = open("config/compositors-template-getter.py")
    compsFile.write("\n")
    compsFile.write(compsGetterPy.read())
    compsGetterPy.close()
    compsFile.close()

    return compsFilePath

def main(args):
    # parsing command line input
    if len(args) < 3:
        print("usage: loader.py <toscaFile> <deploymentInfoFile> <targetFolder>")
        exit(2)
    toscaFile = os.path.abspath(args[0])
    deploymentInfoFile = os.path.abspath(args[1])
    targetFolder = os.path.abspath(args[2])

    os.chdir("loader")

    # parsing input TOSCA and deployment info files
    tosca = parseYaml(toscaFile)
    deploymentInfo = parseYaml(deploymentInfoFile)

    # creating target folder
    if not(os.path.exists(targetFolder)):
        os.mkdir(targetFolder)

    # generating file compositors.py
    comps = generateCompositors(tosca, deploymentInfo)
    targetCompsFilePath = targetFolder + "/compositors.py"
    generateCompositorsPy(comps, targetCompsFilePath)

    # generating file costs.py
    costs = generateCosts(tosca, deploymentInfo)
    targetCostsFilePath = targetFolder + "/costs.py"
    generateCostsPy(costs, targetCostsFilePath)

    os.chdir("..")

main(sys.argv[1:])
