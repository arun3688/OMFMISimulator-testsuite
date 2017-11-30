## status: correct

from OMSimulator import OMSimulator
session=OMSimulator()

session.setLogFile("omsllog.txt")

model = session.newModel()
session.setTempDirectory(".")

session.instantiateFMU(model, "../FMUs/me_BouncingBall.fmu", "BouncingBall")
session.describe(model)

session.setStopTime(model, 2.1)
session.setTolerance(model, 1e-5)
session.setResultFile(model, "me_BouncingBall_res.mat")

session.initialize(model)
session.simulate(model)
session.terminate(model)

session.unload(model)

vars = ["BouncingBall.v", "BouncingBall.der(v)", "BouncingBall.h", "BouncingBall.der(h)", "BouncingBall.ground"]
for var in vars:
  if (1 == session.compareSimulationResults("me_BouncingBall_res.mat", "../ReferenceFiles/me_BouncingBall.csv", var, 1e-2, 1e-4)):
    print(var + " is equal")
  else:
    print(var + " is not equal")


## Result:
## # FMU instances
## BouncingBall
##   - FMI 2.0 ME (solver: euler)
##   - path: ../FMUs/me_BouncingBall.fmu
##   - GUID: {35ad3480-034b-4cbf-9396-c17a51220ee7}
##   - tool: OpenModelica Compiler OMCompiler v1.12.0-dev.395+gdeeabde
##   - input interface:
##   - output interface:
##   - parameters:
##     - parameter e
##     - parameter g
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
## BouncingBall.v is equal
## BouncingBall.der(v) is equal
## BouncingBall.h is equal
## BouncingBall.der(h) is equal
## BouncingBall.ground is equal
## info:    Logging information has been saved to "omsllog.txt"
## endResult
