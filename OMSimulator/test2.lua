-- status: correct

setLogFile("omsllog.txt")

model = newModel()
setTempDirectory(".")

-- instantiate FMUs
instantiateFMU(model, "../FMUs/me_source1.fmu", "sourceA")
instantiateFMU(model, "../FMUs/me_source1.fmu", "sourceB")
instantiateFMU(model, "../FMUs/me_adder1.fmu", "adder1")
instantiateFMU(model, "../FMUs/me_adder1.fmu", "adder2")

-- add connections
addConnection(model, "sourceA.y", "adder1.x1")
addConnection(model, "sourceB.y", "adder1.x2")
addConnection(model, "adder1.y", "adder2.x1")
addConnection(model, "sourceB.y", "adder2.x2")

-- set parameter
setReal(model, "sourceA.A", 0.5)
setReal(model, "sourceA.omega", 2.0)

setStopTime(model, 10.0)

describe(model)

initialize(model)
stepUntil(model, 10.0)
--exportDependencyGraph(model, "test")
--os.execute("gvpr -c \"N[$.degree==0]{delete(root, $)}\" test_simulation.dot | dot -Tpdf -o test_simulation.pdf")
--os.execute("gvpr -c \"N[$.degree==0]{delete(root, $)}\" test_initialization.dot | dot -Tpdf -o test_initialization.pdf")

tcur = getCurrentTime(model)
print("adder1.y at " .. tcur .. ": " .. getReal(model, "adder1.y"))
print("adder2.y at " .. tcur .. ": " .. getReal(model, "adder2.y"))

terminate(model)

unload(model)

-- Result:
-- # FMU instances
-- adder2
--   - FMI 2.0 ME (solver: euler)
--   - path: ../FMUs/me_adder1.fmu
--   - GUID: {bd121558-6b16-4944-819d-dd5fc0b9b8ea}
--   - tool: OpenModelica Compiler OMCompiler v1.12.0-dev.395+gdeeabde
--   - input interface:
--     - input x1
--     - input x2
--   - output interface:
--     - output y
--   - parameters:
-- adder1
--   - FMI 2.0 ME (solver: euler)
--   - path: ../FMUs/me_adder1.fmu
--   - GUID: {bd121558-6b16-4944-819d-dd5fc0b9b8ea}
--   - tool: OpenModelica Compiler OMCompiler v1.12.0-dev.395+gdeeabde
--   - input interface:
--     - input x1
--     - input x2
--   - output interface:
--     - output y
--   - parameters:
-- sourceB
--   - FMI 2.0 ME (solver: euler)
--   - path: ../FMUs/me_source1.fmu
--   - GUID: {a31d622a-f33e-4172-9c76-96665d8d1b60}
--   - tool: OpenModelica Compiler OMCompiler v1.12.0-dev.395+gdeeabde
--   - input interface:
--   - output interface:
--     - output y
--   - parameters:
--     - parameter A
--     - parameter omega
-- sourceA
--   - FMI 2.0 ME (solver: euler)
--   - path: ../FMUs/me_source1.fmu
--   - GUID: {a31d622a-f33e-4172-9c76-96665d8d1b60}
--   - tool: OpenModelica Compiler OMCompiler v1.12.0-dev.395+gdeeabde
--   - input interface:
--   - output interface:
--     - output y
--   - parameters:
--     - parameter A
--     - parameter omega
--
-- # Simulation settings
--   - start time: 0
--   - stop time: 10
--   - tolerance: 0.0001
--   - communication interval: 0.1
--   - result file: <no result file>
--
-- # Composite structure
-- ## Initialization
-- sourceB.y -> adder2.x2
-- sourceB.y -> adder1.x2
-- sourceA.y -> adder1.x1
-- adder1.y -> adder2.x1
--
-- ## Simulation
-- sourceB.y -> adder2.x2
-- sourceB.y -> adder1.x2
-- sourceA.y -> adder1.x1
-- adder1.y -> adder2.x1
--
-- adder1.y at 10.0: -0.087548485525547
-- adder2.y at 10.0: -0.59472013591111
-- info:    Logging information has been saved to "omsllog.txt"
-- endResult
