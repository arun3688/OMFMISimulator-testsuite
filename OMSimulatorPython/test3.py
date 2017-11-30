## status: correct

from OMSimulator import OMSimulator
session=OMSimulator()

session.setLogFile("omsllog.txt")

model = session.newModel()
session.setTempDirectory(".")

# instantiate FMUs
session.instantiateFMU(model, "../FMUs/me_source1.fmu", "sourceA")
session.instantiateFMU(model, "../FMUs/me_source1.fmu", "sourceB")
session.instantiateFMU(model, "../FMUs/me_adder1.fmu", "adder")

# add connections
session.addConnection(model, "sourceA.y", "adder.x1")
session.addConnection(model, "sourceB.y", "adder.x2")

# set parameter
session.setReal(model, "sourceA.A", 0.5)
session.setReal(model, "sourceA.omega", 2.0)

session.setStopTime(model, 0.0)
#setStopTime(model, 10.0)

session.initialize(model)
tcur = session.getCurrentTime(model)
while tcur < 10.0:
  session.doSteps(model, 1)
  tcur = session.getCurrentTime(model)

print("sourceA.y at " + str(tcur) + ": " + str(session.getReal(model, "sourceA.y")))
print("sourceB.y at " + str(tcur) + ": " + str(session.getReal(model, "sourceB.y")))

session.terminate(model)
session.unload(model)

## Result:
## sourceA.y at 10.1: 0.487910258883
## sourceB.y at 10.1: -0.625070648893
## info:    Logging information has been saved to "omsllog.txt"
## endResult
