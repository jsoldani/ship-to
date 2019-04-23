def sum(a,b):
    return a+b

def max(a,b):
    if(a>b):
        return a
    return b

compN1 = {
    "h": sum,
    "v": sum
}

compN2 = {
    "h": max,
    "v": sum
}

compositors = {
    "n1" : compN1,
    "n2" : compN2
}

def compositor(node,direction):
    return compositors[node][direction]
