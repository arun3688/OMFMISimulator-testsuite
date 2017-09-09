-- name: me_test1
-- status: correct

version = getVersion()
-- print(version)
model = newModel()
setTempDirectory(".")

instantiateFMU(model, "../FMUs/me_test1.fmu", "test1")
setSolverMethod(model, "test1", "cvode")
describe(model)

setStopTime(model, 2.1)
setTolerance(model, 1e-5)

initialize(model)
simulate(model)
terminate(model)

unload(model)

-- Result:
-- # FMU instances
-- test1
--   - FMI 2.0 ME (solver: cvode)
--   - path: ../FMUs/me_test1.fmu
--   - GUID: {5daf3328-7e1e-4ed4-af75-84ebb83eb29e}
--   - tool: OpenModelica Compiler OMCompiler v1.12.0-dev.395+gdeeabde
--   - input interface:
--   - output interface:
--   - parameters:
--
-- # Simulation settings
--   - start time: 0
--   - stop time: 1
--   - tolerance: 0.0001
--   - communication interval: 0.1
--   - result file: <no result file>
--
-- # Composite structure
-- ## Initialization
--
-- ## Simulation
--
-- endResult
