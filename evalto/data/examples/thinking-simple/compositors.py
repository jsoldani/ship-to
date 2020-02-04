def sum(a,b):
    return a+b

bothSumming = {
    "h": sum,
    "v": sum
}

compositors = {
    "bottom": bothSumming,
    "toskerNodesContainer": bothSumming
}

def compositor(sort,direction):
    return compositors[sort][direction]
