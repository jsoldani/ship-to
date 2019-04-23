costs = {
    "api": "fifteen.four",
    "bottom": "zero",
    "dbvolume": 0.4,
    "gui": 2.1,
    "mongodb": 165.0, #tag: 3.6.12
    "node": 23, #tag: 8.16.0-alpine
    "maven": 210.0 #tag: 3-jdk-13-alpine
}

def cost(node):
    return costs[node]
