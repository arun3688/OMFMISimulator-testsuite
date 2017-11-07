
# status: correct

from OMSimulatorPython import OMSimulatorPython
session=OMSimulatorPython()

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

# -- Result:
# -- adder1.y at 2.1: 0.54162379186909
# -- adder2.y at 2.1: 1.564940364302
# -- info:    Logging information has been saved to "omsllog.txt"
# -- endResult
