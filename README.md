# ShipTo

EvalTo implements a graph transformation-based for determining the overall resource consumption of the software stacks forming the topology of a TOSCA application, and it determines the nodes in an edge cluster that can be used to host each of such stacks.

## Prerequisites
To effectively be executed on a `bash` shell, EvalTo requires such shell to support the following commands:
* `python` (version 3.4 or higher),
* `pip`, and
* `swipl`.

The available installation of Python must also be equipped with the following Python packages:
* `pyswip` and 
* `tosca-parser`.

Both above packages can be easily installed by typing `sudo pip install <packageName>`.

## Using ShipTo

### Preparing the input 

To effectively run **ShipTo**, two artifacts have to provided as input:
1. A TOSCA specification of the _topology of the application_ to be deployed,
2. A YAML file providing _deployment-specific information_, i.e., (a) the resource `consumption` (in terms of `memory` and `storage`) of the components forming the application, and (b) listing the `clusterNodes` forming the edge cluster where to deploy the application, together with the `memory` and `storage` they feature. 

Templates for both 1 and 2 are available in the [data/templates](https://github.com/jsoldani/ship-to/tree/master/data/templates) subfolder. Concrete examples are instead available in the [data/examples](https://github.com/jsoldani/ship-to/tree/master/data/examples/) subfolder.

### Running ShipTo
**ShipTo** is designed to run on `bash` shells. To compute the feasible deployment for an application on a cluster, just type the following command
```
python shipto.py <toscaFile> <deploymentInformationFile>
```
when positioned in the main folder of the current repository. Note: 
* `<toscaFile>` is the relative/absolute path to the YAML file specifying the application topology in TOSCA, while
* `<deploymentInformationFile>` is the relative/absolute path to the YAML file providing _deployment-specific information_ (see 2 in _Preparing the input_). 

## About ShipTo

The machinery implemented by ShipTo has been defined in the research paper:
 > _J. Soldani. <br>
 > **Finding feasible application deployments in edge clusters, with limited resources.** <br>
 > [Submitted for publication]_

If you wish to exploit EvalTo to carry out research activities, or if you wish to reuse its sources, please properly cite the above mentioned paper. Below you can find the BibTex reference:
```
TBA
```
