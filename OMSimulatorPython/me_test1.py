## status: correct

import sys
sys.path.append('../../install/lib')

from OMSimulator import OMSimulator
session=OMSimulator()

session.setLogFile("omsllog.txt")

model = session.newModel()
session.setTempDirectory(".")

session.instantiateFMU(model, "../FMUs/me_test1.fmu", "test1")
session.setSolverMethod(model, "test1", "cvode")
session.describe(model)

session.setStopTime(model, 2.1)
session.setTolerance(model, 1e-5)
session.setResultFile(model, "me_test1_res.mat")

session.initialize(model)
session.simulate(model)
session.terminate(model)

session.unload(model)

vars = ["test1.x", "test1.der(x)"]
for var in vars:
  if (1 == session.compareSimulationResults("me_test1_res.mat", "../ReferenceFiles/me_test1.mat", var, 1e-2, 1e-4)):
    print(var + " is equal")
  else:
    print(var + " is not equal")


## Result:
## # FMU instances
## test1
##   - FMI 2.0 ME (solver: cvode)
##   - path: ../FMUs/me_test1.fmu
##   - GUID: {5daf3328-7e1e-4ed4-af75-84ebb83eb29e}
##   - tool: OpenModelica Compiler OMCompiler v1.12.0-dev.395+gdeeabde
##   - input interface:
##   - output interface:
##   - parameters:
##
## # Lookup tables
##
## # Simulation settings
##   - start time: 0
##   - stop time: 1
##   - tolerance: 0.0001
##   - communication interval: 0.1
##   - result file: <no result file>
##
## # Composite structure
## ## External inputs
##
## ## Initialization
##
## ## Simulation
##
## test1.x is equal
## test1.der(x) is equal
## info:    Logging information has been saved to "omsllog.txt"
## endResult
