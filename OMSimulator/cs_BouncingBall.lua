-- name: cs_BouncingBall
-- status: correct

version = getVersion()
-- print(version)

model = newModel()
setTempDirectory(".")

instantiateFMU(model, "../FMUs/cs_BouncingBall.fmu", "BouncingBall")
setStopTime(model, 5.0)
setTolerance(model, 1e-5)
setCommunicationInterval(model, 1e-2)
setVariableFilter(model, "BouncingBall", ".*")
setResultFile(model, "cs_BouncingBall_res.mat")

describe(model)

initialize(model)
simulate(model)
terminate(model)

unload(model)

vars = {"BouncingBall.v", "BouncingBall.der(v)", "BouncingBall.h", "BouncingBall.der(h)", "BouncingBall.ground"}
for _,var in ipairs(vars) do
  if 1 == compareSimulationResults("cs_BouncingBall_res.mat", "../ReferenceFiles/cs_BouncingBall.csv", var, 1e-2, 1e-4) then
    print(var .. " is equal")
  else
    print(var .. " is not equal")
  end
end

-- Result:
-- # FMU instances
-- BouncingBall
--   - FMI 2.0 CS
--   - path: ../FMUs/cs_BouncingBall.fmu
--   - GUID: {ed0c3e8c-c48f-4995-b80b-eb1d54c9737b}
--   - tool: OpenModelica Compiler OMCompiler v1.12.0-dev.395+gdeeabde
--   - input interface:
--   - output interface:
--   - parameters:
--     - parameter e
--     - parameter g
--
-- # Simulation settings
--   - start time: 0
--   - stop time: 5
--   - tolerance: 1e-05
--   - communication interval: 0.01
--   - result file: cs_BouncingBall_res.mat
--
-- # Composite structure
-- ## Initialization
--
-- ## Simulation
--
-- BouncingBall.v is equal
-- BouncingBall.der(v) is equal
-- BouncingBall.h is equal
-- BouncingBall.der(h) is equal
-- BouncingBall.ground is equal
-- endResult
