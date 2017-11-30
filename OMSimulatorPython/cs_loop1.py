## status: correct

from OMSimulator import OMSimulator
session=OMSimulator()

session.setLogFile("omsllog.txt")

model = session.newModel()
session.setTempDirectory(".")

session.instantiateFMU(model, "../FMUs/cs.loop1.A.fmu", "A")
session.instantiateFMU(model, "../FMUs/cs.loop1.B.fmu", "B")
session.instantiateFMU(model, "../FMUs/cs.loop1.P.fmu", "P")

# add connections
session.addConnection(model, "A.y", "B.u")
session.addConnection(model, "B.y", "A.u")
session.addConnection(model, "P.y", "A.p")
session.addConnection(model, "P.y", "B.p")

session.setResultFile(model, "cs_loop1_res.mat")
session.setStopTime(model, 0.5)
session.setCommunicationInterval(model, 1e-2)
session.setTolerance(model, 1e-6)

session.describe(model)

session.initialize(model)
session.simulate(model)
session.terminate(model)

session.unload(model)

vars = ["A.y", "B.y"]
for var in vars:
  if (1 == session.compareSimulationResults("cs_loop1_res.mat", "../ReferenceFiles/cs_loop1.mat", var, 1e-4, 1e-2)):
    print(var + " is equal")
  else:
    print(var + " is not equal")


## Result:
## # FMU instances
## P
##   - FMI 2.0 CS
##   - path: ../FMUs/cs.loop1.P.fmu
##   - GUID: {4cca3b30-6b93-42f0-924c-1ab12147a132}
##   - tool: OpenModelica Compiler OMCompiler v1.13.0-dev.70+g702501a
##   - input interface:
##   - output interface:
##     - output y
##   - parameters:
## B
##   - FMI 2.0 CS
##   - path: ../FMUs/cs.loop1.B.fmu
##   - GUID: {4b294516-129c-476d-be07-72947b187382}
##   - tool: OpenModelica Compiler OMCompiler v1.13.0-dev.70+g702501a
##   - input interface:
##     - input p
##     - input u
##   - output interface:
##     - output y
##   - parameters:
## A
##   - FMI 2.0 CS
##   - path: ../FMUs/cs.loop1.A.fmu
##   - GUID: {cb59288a-46a8-4e75-858b-dac5f2eac8a7}
##   - tool: OpenModelica Compiler OMCompiler v1.13.0-dev.70+g702501a
##   - input interface:
##     - input p
##     - input u
##   - output interface:
##     - output y
##   - parameters:
##
## # Lookup tables
##
## # Simulation settings
##   - start time: 0
##   - stop time: 0.5
##   - tolerance: 1e-06
##   - communication interval: 0.01
##   - result file: cs_loop1_res.mat
##
## # Composite structure
## ## External inputs
##
## ## Initialization
## P.y -> B.p
## P.y -> A.p
## {B.y -> A.u; A.y -> B.u}
##
## ## Simulation
## P.y -> B.p
## P.y -> A.p
## {B.y -> A.u; A.y -> B.u}
##
## stdout            | info    | The initialization finished successfully without homotopy method.
## stdout            | info    | The initialization finished successfully without homotopy method.
## stdout            | info    | The initialization finished successfully without homotopy method.
## A.y is equal
## B.y is equal
## info:    2 warnings
## info:    0 errors
## info:    Logging information has been saved to "omsllog.txt"
## endResult
