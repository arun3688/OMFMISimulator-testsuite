## status: correct

import sys
sys.path.append('../../install/lib')

from OMSimulator import OMSimulator
session=OMSimulator()

session.setLogFile("omsllog.txt")

model = session.newModel()
session.setTempDirectory(".")

# instantiate FMU
session.instantiateFMU(model, "../FMUs/me_HelloWorld.fmu", "HelloWorld")

# set parameter
session.setReal(model, "HelloWorld.x_start", 1.0)
session.setReal(model, "HelloWorld.a", -1.0)
session.setStopTime(model, 1.0)
# initialize and simulate
session.initialize(model)
session.stepUntil(model, 1.0)
tcur = session.getCurrentTime(model)

print("Parametrization 1: HelloWorld.x at " + str(tcur) + ":" + str(session.getReal(model, "HelloWorld.x")))

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

print("Parametrization 1: HelloWorld.x at " + str(tcur) + ":" + str(session.getReal(model, "HelloWorld.x")))


session.terminate(model)

session.unload(model)

## Result:
## Parametrization 1: HelloWorld.x at 1.0:0.366032341273
## Parametrization 1: HelloWorld.x at 1.0:0.0663097779474
## info:    Logging information has been saved to "omsllog.txt"
## endResult
