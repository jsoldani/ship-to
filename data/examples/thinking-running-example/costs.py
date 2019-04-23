costs = {
    "rest_api": {
        "memory": 139.2,
        "storage": 15.4
    },
    "database": {
        "memory": 56.9,
        "storage": 500.0
    },
    "gui": {
        "memory": 19.8,
        "storage": 2.1
    },
    "httpd": {
        "memory": 5.9,
        "storage": 643.0
    },
    "java": {
        "memory": 1.5,
        "storage": 178.0
    },
    "maven": {
        "memory": 128.0,
        "storage": 20.9
    },
    "mongo": {
        "memory": 39.4,
        "storage": 381.0
    },
    "php": {
        "memory": 64.0,
        "storage": 131.1
    },
    "storage": {
        "memory": 0.1,
        "storage": 0.4
    },
    "front_vm": [
        {
            "name": "aws.t3.nano.usw",
            "memory": 500.0,
            "storage": 500.0,
            "cost": 0.0052
        },{
            "name": "aws.t2.nano.usw",
            "memory": 500.0,
            "storage": 1024.0,
            "cost": 0.0058
        },{
            "name": "aws.t3.micro.usw",
            "memory": 1024.0,
            "storage": 1024.0,
            "cost": 0.0104
        },{
            "name": "aws.t2.micro.usw",
            "memory": 1024.0,
            "storage": 2048.0,
            "cost": 0.0116
        }
    ],
    "back_vm": [
        {
            "name": "azure.b1s.usc",
            "memory": 1024.0,
            "storage": 1024.0,
            "cost": 0.0016
        },{
            "name": "azure.b2s.eun",
            "memory": 2048.0,
            "storage": 2048.0,
            "cost": 0.0045
        },{
            "name": "aws.t3.micro.usw",
            "memory": 1024.0,
            "storage": 1024.0,
            "cost": 0.0104
        },{
            "name": "aws.t2.micro.usw",
            "memory": 1024.0,
            "storage": 2048.0,
            "cost": 0.0116
        },{
            "name": "aws.t3.small.eun",
            "memory": 2048.0,
            "storage": 2048.0,
            "cost": 0.0236
        }
    ],
    "bottom": {
        "min": 0.0,
        "max": 0.0
    }
}

def cost(node):
    return costs[node]
