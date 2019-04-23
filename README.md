# EvalTo

EvalTo implements a toolchain for running cost estimation problems (see _About_).

## Prerequisites
To effectively be executed on a `bash` shell, EvalTo requires such shell to support the following commands:
* `python` (version 3.4 or higher),
* `pip`, and
* `swipl`.

The available installation of Python must also be equipped with the following Python packages:
* `pyswip` and 
* `tosca-parser`.

Both above packages can be easily installed by typing `sudo pip install <packageName>`.

## Using EvalTo

### Defining a cost estimation problem 

To define a cost estimation problem, three artifacts have to be developed:
1. A TOSCA specification of the _topology of the application_ on which the problem is to be defined,
2. A Python module defining the _compositors_ to be used to combine the costs associated with the components forming the application, and
3. A Python module associating the components forming the application with their _costs_.

Templates for 2 and 3 are available in the [data/templates](https://github.com/di-unipi-socc/eval-to/tree/master/data/templates) subfolder. Complete examples of cost estimation problems are instead available in the [data/examples](https://github.com/di-unipi-socc/eval-to/tree/master/data/examples) subfolder.

### Running EvalTo
EvalTo is designed to run on `bash` shells. To run a cost estimation problem (defined as illustrated above), just type the following command
```
python evalto.py <toscaFile> <compositorsFile.py> <costsFile.py>
```
when positioned in the main folder of the current repository. Note: 
* `<toscaFile>` is the relative/absolute path to the YAML file specifying the application topology in TOSCA,
* `<compositorsFile.py>` is the relative/absolute path to the Python module defining the cost compositors, while
* `<costsFile.py>` is the relative/absolute path to the Python module associating the components forming the application with their costs. 

## About EvalTo

The machinery implemented by EvalTo has been defined in the research paper:
 > _A. Brogi, A. Corradini, J. Soldani. <br>
 > **Estimating costs of multi-component enterprise applications.** <br>
 > [Submitted for publication]_

If you wish to exploit EvalTo to carry out research activities, or if you wish to reuse its sources, please properly cite the above mentioned paper. Below you can find the BibTex reference:
```
TBA
```
