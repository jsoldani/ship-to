def update_placement(consumption,placement):
    p = placement[0]
    # updating resource requirements
    if consumption["memory"] > p["memory"]:
        p["memory"] = consumption["memory"]
    p["storage"] = p["storage"] + consumption["storage"]

    # reducing possible placements to feasible ones
    reducedClusterNodes = {}
    for clusterNodeName in p["clusterNodes"]:
        clusterNode = p["clusterNodes"][clusterNodeName]
        if consumption["memory"] < clusterNode["memory"] and consumption["storage"] < clusterNode["storage"]:
            reducedClusterNodes[clusterNodeName] = p["clusterNodes"][clusterNodeName]
    p["clusterNodes"] = reducedClusterNodes

    return [p]

def union_placements(placement1,placement2):
    return placement1 + placement2

def sum_consumptions(consumption1,consumption2):
    sum = {}
    for key in consumption1:
        sum[key] = consumption1[key] + consumption2[key]
    return sum
