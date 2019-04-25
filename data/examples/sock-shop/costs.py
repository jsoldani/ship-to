amazonT3Offerings = [
    {
        "name": "aws.t3.nano.usw",
        "memory": 500.0,
        "storage": 500.0,
        "cost": 0.0052
    }, {
        "name": "aws.t3.micro.usw",
        "memory": 1024.0,
        "storage": 1024.0,
        "cost": 0.0104
    }, {
        "name": "aws.t3.small.eun",
        "memory": 2048.0,
        "storage": 2048.0,
        "cost": 0.0236
    }
]

amazonT2Offerings = [
    {
        "name": "aws.t2.nano.usw",
        "memory": 500.0,
        "storage": 1024.0,
        "cost": 0.0058
    }, {
        "name": "aws.t2.micro.usw",
        "memory": 1024.0,
        "storage": 2048.0,
        "cost": 0.0116
    }
]

azureOfferings = [
    {
        "name": "azure.b1s.usc",
        "memory": 1024.0,
        "storage": 1024.0,
        "cost": 0.0016
    }, {
        "name": "azure.b2s.eun",
        "memory": 2048.0,
        "storage": 2048.0,
        "cost": 0.0045
    }
]



costs = {
    "edge_router" : {
        "memory": 6.49, # docker stats
        "storage": 21.9 # docker image size
    },
    "frontend": {
        "memory": 48.83, # RSS of running process
        "storage": 66.6 # disk usage of app folder
    },
    "frontend_container": {
        "memory": 20.28, # docker stats
        "storage": 71 # size of node:10-alpine
    },
    "frontend_vm": amazonT2Offerings + amazonT3Offerings + azureOfferings,
    "catalogue": {
        "memory": 6.65, # RSS of running process
        "storage": 13.6 # size of go compiled program
    },
    "catalogue_container": {
        "memory": 3.13, # docker stats
        "storage": 676 # size of golang:1.7
    },
    "catalogue_db": {
        "memory": 120.9, # docker stats
        "storage": 400 # docker image size
    },
    "catalogue_vm": amazonT2Offerings + amazonT3Offerings + azureOfferings,
    "orders": {
        "memory": 254.88, # RSS of running process
        "storage": 24.7 # jar size
    },
    "orders_container": {
        "memory": 2.82, # docker stats
        "storage": 57 # size of weaveworksdemos/msd-java:jre-latest
    },
    "orders_db": {
        "memory": 14.56, # docker stats
        "storage": 425 # size of mongo:3.4
    },
    "orders_vm": amazonT2Offerings + amazonT3Offerings + azureOfferings,
    "users": {
        "memory": 7.95, # RSS of running process
        "storage": 14.1 # size of go compiled program
    },
    "users_container": {
        "memory": 3.38, # docker stats
        "storage": 241 # size of golang:1.7-alpine
    },
    "users_db": {
        "memory": 16.47, # docker stats
        "storage": 717 # docker image size
    },
    "users_vm": amazonT2Offerings + amazonT3Offerings + azureOfferings,
    "carts": {
        "memory": 255.85, # RSS of running process
        "storage": 24.6 # jar size
    },
    "carts_container": {
        "memory": 1.65, # docker stats
        "storage": 57 # size of weaveworksdemos/msd-java:jre-latest
    },
    "carts_db": {
        "memory": 26.81, # docker stats
        "storage": 425 # size of mongo:3.4
    },
    "carts_vm": amazonT2Offerings + amazonT3Offerings + azureOfferings,
    "payment": {
        "memory": 2.09, # docker stats
        "storage": 32.5 # docker image size
    },
    "payment_vm": amazonT2Offerings + amazonT3Offerings + azureOfferings,
    "shipping": {
        "memory": 248.05, # RSS of running process
        "storage": 25.1 # jar size
    },
    "shipping_container": {
        "memory": 1.75, # docker stats
        "storage": 57 # weaveworksdemos/msd-java:jre-latest
    },
    "rabbitmq": {
        "memory": 33.21, # docker stats
        "storage": 179 # size of rabbitmq:3.6.8
    },
    "queue_master": {
        "memory": 139.2, # docker stats
        "storage": 179 # docker image size
    },
    "shipping_vm": amazonT2Offerings + amazonT3Offerings + azureOfferings,
    "bottom": {
        "min": 0.0,
        "max": 0.0
    }
}


def cost(node):
    return costs[node]
