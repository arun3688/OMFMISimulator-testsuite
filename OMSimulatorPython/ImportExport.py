## status: correct

from OMSimulator import OMSimulator
session=OMSimulator()

session.setLogFile("omsllog.txt")

session.setTempDirectory(".")
model = session.newModel()

## instantiate FMUs
session.instantiateFMU(model, "../FMUs/me_source1.fmu", "sourceA")
session.instantiateFMU(model, "../FMUs/me_source1.fmu", "sourceB")
session.instantiateFMU(model, "../FMUs/me_adder1.fmu", "adder")

## add connections
session.addConnection(model, "sourceA.y", "adder.x1")
session.addConnection(model, "sourceB.y", "adder.x2")

## set parameter
session.setReal(model, "sourceA.A", 0.5)
session.setReal(model, "sourceA.omega", 2.0)

session.setStartTime(model, 0.0)
session.setStopTime(model, 10.0)
session.setTolerance(model, 1e-5)

session.exportXML(model, "ImportExport.xml")
session.unload(model)


model2 = session.loadModel("ImportExport.xml")
session.describe(model2)
session.unload(model2)

## Result:
## # FMU instances
## sourceA
##   - FMI 2.0 ME (solver: euler)
##   - path: ../FMUs/me_source1.fmu
##   - GUID: {a31d622a-f33e-4172-9c76-96665d8d1b60}
##   - tool: OpenModelica Compiler OMCompiler v1.12.0-dev.395+gdeeabde
##   - input interface:
##   - output interface:
##     - output y
##   - parameters:
##     - parameter A
##     - parameter omega
## adder
##   - FMI 2.0 ME (solver: euler)
##   - path: ../FMUs/me_adder1.fmu
##   - GUID: {bd121558-6b16-4944-819d-dd5fc0b9b8ea}
##   - tool: OpenModelica Compiler OMCompiler v1.12.0-dev.395+gdeeabde
##   - input interface:
##     - input x1
##     - input x2
##   - output interface:
##     - output y
##   - parameters:
## sourceB
##   - FMI 2.0 ME (solver: euler)
##   - path: ../FMUs/me_source1.fmu
##   - GUID: {a31d622a-f33e-4172-9c76-96665d8d1b60}
##   - tool: OpenModelica Compiler OMCompiler v1.12.0-dev.395+gdeeabde
##   - input interface:
##   - output interface:
##     - output y
##   - parameters:
##     - parameter A
##     - parameter omega
##
## # Lookup tables
##
## # Simulation settings
##   - start time: 0
##   - stop time: 10
##   - tolerance: 1e-05
##   - communication interval: 0.1
##   - result file: ImportExport_res.mat
##
## # Composite structure
## ## External inputs
##
## ## Initialization
## sourceA.y -> adder.x1
## sourceB.y -> adder.x2
##
## ## Simulation
## sourceA.y -> adder.x1
## sourceB.y -> adder.x2
##
## info:    Logging information has been saved to "omsllog.txt"
## endResult
