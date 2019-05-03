def fun1(a,b):
    return a+b # example function: sum

def fun2(a,b):
    return a*b # example function: product

compositors = {
    "nodeType1": {
        "h": fun1,
        "v": fun2
    },
    "nodeType2": {
        "h": fun1,
        "v": fun1
    }
}

def compositor(sort,direction):
    return compositors[sort][direction]
