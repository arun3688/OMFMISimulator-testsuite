-- name: me_BouncingBall
-- status: correct

version = getVersion()
-- print(version)

model = newModel()
setTempDirectory(".")

instantiateFMU(model, "../FMUs/me_BouncingBall.fmu", "BouncingBall")
describe(model)

setStopTime(model, 2.1)
setTolerance(model, 1e-5)

initialize(model)
simulate(model)
terminate(model)

unload(model)

-- Result:
-- # FMU instances
-- BouncingBall
--   - FMI 2.0 ME (solver: euler)
--   - path: ../FMUs/me_BouncingBall.fmu
--   - GUID: {35ad3480-034b-4cbf-9396-c17a51220ee7}
--   - tool: OpenModelica Compiler OMCompiler v1.12.0-dev.395+gdeeabde
--   - input interface:
--   - output interface:
--   - parameters:
--     - parameter e
--     - parameter g
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
