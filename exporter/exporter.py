import json
import os
import sys
import yaml

def main(args):
    # parsing command line input
    if len(args) < 2:
        print("usage: exporter.py <evaltoOutput> <targetYaml>")
        exit(2)
    evaltoOutput = os.path.abspath(args[0])
    targetYaml = os.path.abspath(args[1])

    # reading evalto output
    evaltoOutputFile = open(evaltoOutput)
    output = json.load(evaltoOutputFile)
    evaltoOutputFile.close()

    # creating output YAML file
    shapedOutput = {}
    for placement in output:
        computeNode = placement["name"]
        shapedOutput[computeNode] = {}
        shapedOutput[computeNode]["required_memory"] = placement["memory"]
        shapedOutput[computeNode]["required_storage"] = placement["storage"]
        shapedOutput[computeNode]["feasible_deployments"] = placement["clusterNodes"]
    targetYamlFile = open(targetYaml, "w")
    yaml.dump(shapedOutput,targetYamlFile)
    targetYamlFile.close()

main(sys.argv[1:])
