# TODO: Fill in the "compositor" dictionary to associate the node types in a topology with cost compositors
compositors = { }

def compositor(node,direction):
    return compositors[node][direction]
