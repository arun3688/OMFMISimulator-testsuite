# status: correct

from OMSimulatorPython import OMSimulatorPython
session=OMSimulatorPython()

session.setLogFile("omsllog.txt")

model = session.newModel()
session.setTempDirectory(".")

# instantiate FMU
session.instantiateFMU(model, "../FMUs/cs_HelloWorld.fmu", "HelloWorld")

# set parameter
session.setReal(model, "HelloWorld.x_start", 1.0)
session.setReal(model, "HelloWorld.a", -1.0)
session.setStopTime(model, 1.0)
# initialize and simulate
session.initialize(model)
session.stepUntil(model, 1.0)
tcur = session.getCurrentTime(model)
print("Parametrization 1: HelloWorld.x at " + str(tcur) + ": " + str(session.getReal(model, "HelloWorld.x")))

# reset FMU
session.reset(model)
# set parameter
session.setReal(model, "HelloWorld.x_start", 0.5)
session.setReal(model, "HelloWorld.a", -2.0)
session.setStopTime(model, 1.0)
# initialize and simulate
session.initialize(model)
session.stepUntil(model, 1.0)
tcur = session.getCurrentTime(model)
print("Parametrization 2: HelloWorld.x at " + str(tcur) + ": " + str(session.getReal(model, "HelloWorld.x")))

session.terminate(model)
session.unload(model)

# Result:
# Parametrization 1: HelloWorld.x at 1.0: 0.36603234127323
# Parametrization 2: HelloWorld.x at 1.0: 0.066309777947377
# info:    Logging information has been saved to "omsllog.txt"
# endResult
