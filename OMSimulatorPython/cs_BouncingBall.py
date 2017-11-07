#status: correct

from OMSimulatorPython import OMSimulatorPython
session=OMSimulatorPython()

session.setLogFile("omsllog.txt")

model = session.newModel()
session.setTempDirectory(".")

session.instantiateFMU(model, "../FMUs/cs_BouncingBall.fmu", "BouncingBall")
session.setStopTime(model, 5.0)
session.setTolerance(model, 1e-5)
session.setCommunicationInterval(model, 1e-2)
session.setVariableFilter(model, "BouncingBall", ".*")
session.setResultFile(model, "cs_BouncingBall_res.mat")

session.describe(model)

session.initialize(model)
session.simulate(model)
session.terminate(model)

session.unload(model)

vars = ["BouncingBall.v", "BouncingBall.der(v)", "BouncingBall.h", "BouncingBall.der(h)", "BouncingBall.ground"]
for var in vars:
  if (1 == session.compareSimulationResults("cs_BouncingBall_res.mat", "../ReferenceFiles/cs_BouncingBall.csv", var, 1e-2, 1e-4)):
    print(var + " is equal")
  else:
    print(var + " is not equal")
 

# Result:
# # FMU instances
# BouncingBall
#   - FMI 2.0 CS
#   - path: ../FMUs/cs_BouncingBall.fmu
#   - GUID: {ed0c3e8c-c48f-4995-b80b-eb1d54c9737b}
#   - tool: OpenModelica Compiler OMCompiler v1.12.0-dev.395+gdeeabde
#   - input interface:
#   - output interface:
#   - parameters:
#     - parameter e
#     - parameter g
#
# # Lookup tables
#
# # Simulation settings
#   - start time: 0
#   - stop time: 5
#   - tolerance: 1e-05
#   - communication interval: 0.01
#   - result file: cs_BouncingBall_res.mat
#
# # Composite structure
# ## External inputs
#
# ## Initialization
#
# ## Simulation
#
# BouncingBall.v is equal
# BouncingBall.der(v) is equal
# BouncingBall.h is equal
# BouncingBall.der(h) is equal
# BouncingBall.ground is equal
# info:    Logging information has been saved to "omsllog.txt"
# endResult
