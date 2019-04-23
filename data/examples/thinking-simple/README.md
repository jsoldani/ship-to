## thinking-simple example

Cost estimation problem for evaluating the total storage (in MBs) required by a deployment of the Thinking application.
* `thinking.yml` specifies the application deployment in TOSCA
* `compositors.py` specifies the functions to be used to compose the costs associated with the components of the Thinking application
* `costs.py` specifies the costs associated with the components of the Thinking application (i.e., the MBs of storage they occupy)

To run the cost estimation problem, just go to the main folder of the project, and type
``python evalto.py .\data\examples\thinking-simple\thinking.yml .\data\examples\thinking-simple\compositors.py .\data\examples\thinking-simple\costs.py``
