## status: correct

from OMSimulator import OMSimulator
session=OMSimulator()

session.setLogFile("omsllog.txt")

session.setTempDirectory(".")
model =session.loadModel('ConnectedFmu.xml')

session.initialize(model)
session.simulate(model)
tcur = session.getCurrentTime(model)
print "python test", tcur
print("adder1.y at  .. " + str(tcur) + ": " + str(session.getReal(model, "adder1.y")))
print("adder2.y at  .. " + str(tcur) + ": " + str(session.getReal(model, "adder2.y")))

session.terminate(model)
session.unload(model)

## Result:
## python test 2.1
## adder1.y at  .. 2.1: 0.541623791869
## adder2.y at  .. 2.1: 1.5649403643
## info:    Logging information has been saved to "omsllog.txt"
## endResult
