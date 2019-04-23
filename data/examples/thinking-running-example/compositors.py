def pairwiseSum(a,b):
    newCost = {}
    newCost["memory"] = a["memory"] + b["memory"]
    newCost["storage"] = a["storage"] + b["storage"]
    return newCost

def compatibleOfferings(reqs,offerings):
    newOfferings = []
    for off in offerings:
        if off["memory"] >= reqs["memory"] and off["storage"] >= reqs["storage"]:
            newOfferings.append(off)
    return newOfferings

def min(offerings):
    m = offerings[0]
    for off in offerings:
        if off["cost"] < m["cost"]:
            m = off
    return m

def max(offerings):
    M = offerings[0]
    for off in offerings:
        if off["cost"] > M["cost"]:
            M = off
    return M

def minMaxOfferings(offerings1,offerings2):
    min1 = min(offerings1)
    max1 = max(offerings1)
    min2 = min(offerings2)
    max2 = max(offerings2)
    newOfferings = []
    newOfferings.append({
        "name": "m",
        "memory": None,
        "storage": None,
        "cost": min1["cost"] + min2["cost"]
    })
    newOfferings.append({
        "name": "M",
        "memory": None,
        "storage": None,
        "cost": max1["cost"] + max2["cost"]
    })
    return newOfferings

def sumOfferings(offerings,total):
    minOff = min(offerings)
    maxOff = max(offerings)
    newTotal = {
        "min": total["min"] + minOff["cost"],
        "max": total["max"] + maxOff["cost"]
    }
    return newTotal

compositors = {
    "evaltoNodesContainer": {
        "h": pairwiseSum,
        "v": pairwiseSum
    },
    "evaltoNodesVM": {
        "h": pairwiseSum,
        "v": compatibleOfferings
    },
    "bottom": {
        "h": minMaxOfferings,
        "v": sumOfferings
    }
}

def compositor(node,direction):
    return compositors[node][direction]
