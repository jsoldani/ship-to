# EvalTo

Toolchain for running cost estimation problems

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

TBD

### Running EvalTo
EvalTo is designed to run on `bash` shells. To run a cost estimation problem (defined as illustrated above), just type the following command
```
python evalto.py <toscaFile> <compositorsFile.py> <costsFile.py>
```
when positioned in the main folder of the current repository.

## About EvalTo

The machinery implemented by EvalTo has been defined in the research paper:
 > _A. Brogi, A. Corradini, J. Soldani. <br>
 > **Estimating costs of multi-component enterprise applications.** <br>
 > [Submitted for publication]_

If you wish to exploit EvalTo to carry out research activities, or if you wish to reuse its sources, please properly cite the above mentioned paper. Below you can find the BibTex reference:
```
TBA
```
