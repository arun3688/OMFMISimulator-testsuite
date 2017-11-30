## status: correct

from OMSimulator import OMSimulator
session=OMSimulator()

session.setLogFile("omsllog.txt")

model = session.newModel()
session.setTempDirectory(".")

session.instantiateFMU(model, "../FMUs/cs_test1.fmu", "test1")
session.describe(model)

session.setStopTime(model, 2.1)
session.setTolerance(model, 1e-5)
session.setResultFile(model, "cs_test1_res.mat")

session.initialize(model)
session.simulate(model)
session.terminate(model)

session.unload(model)

vars = ["test1.x"]
for var in vars:
  if (1 == session.compareSimulationResults("cs_test1_res.mat", "../ReferenceFiles/cs_test1.mat", var, 1e-2, 1e-4)):
    print(var + " is equal")
  else:
    print(var + " is not equal")

## Result:
## # FMU instances
## test1
##   - FMI 2.0 CS
##   - path: ../FMUs/cs_test1.fmu
##   - GUID: {e72ab90f-3c54-4c60-a423-177dbaddd14c}
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
## info:    Logging information has been saved to "omsllog.txt"
## endResult
