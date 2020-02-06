import os
import json
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

def generateCostsPy(costs):
    costsFilePath = os.getcwd() + "/tmp/costs.py"
    costsFile = open(costsFilePath, "w+")

    costsFile.write("costs = " + json.dumps(costs))

    costsGetterPy = open("config/costs-template-getter.py")
    costsFile.write("\n")
    costsFile.write(costsGetterPy.read())
    costsGetterPy.close()

    costsFile.close()

    return costsFilePath


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

def generateCompositorsPy(comps):
    compsFilePath = os.getcwd() + "/tmp/compositors.py"
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

#compositors = {"bottom": {"h": "placements_union", "v": "placements_union"}, "shipto.nodes.Compute": {"h": "sum_consumptions", "v": "placement"}, "shipto.nodes.Container": {"h": "sum_consumptions", "v": "sum_consumptions"}, "shipto.nodes.Software": {"h": "sum_consumptions", "v": "sum_consumptions"}, "shipto.nodes.WebApplication": {"h": "sum_consumptions", "v": "sum_consumptions"}, "shipto.nodes.Volume": {"h": "sum_consumptions", "v": "sum_consumptions"}, "shipto.nodes.Database": {"h": "sum_consumptions", "v": "sum_consumptions"}}

    compsGetterPy = open("config/compositors-template-getter.py")
    compsFile.write("\n")
    compsFile.write(compsGetterPy.read())
    compsGetterPy.close()
    compsFile.close()

    return compsFilePath

def main(args):
    # check and parse command line arguments
    if len(args) < 2:
        print("usage: shipto.py <toscaFile> <deploymentInfoFile>")
        exit(2)
    toscaFile = os.path.abspath(args[0])
    deploymentInfoFile = os.path.abspath(args[1])

    # configuring desired evalto instance
    print("Configuring solver...", end="")
    tosca = parseYaml(toscaFile)
    deploymentInfo = parseYaml(deploymentInfoFile)

    if not(os.path.exists("tmp")):
        os.mkdir("tmp")

    costs = generateCosts(tosca, deploymentInfo)
    costsFilePath = generateCostsPy(costs)

    comps = generateCompositors(tosca, deploymentInfo)
    compsFilePath = generateCompositorsPy(comps)

    print("done!")

    # launching evalto topology from TOSCA to prolog
    out = os.system("python evalto/evalto.py " + toscaFile + " " + compsFilePath + " " + costsFilePath)

    # printing results
    print("** Identified feasible application deployments **")
    resultTxt = os.getcwd() + "/evalto/output.txt"
    resultFile = open(resultTxt)
    print(resultFile.read())
    resultFile.close()

main(sys.argv[1:])
