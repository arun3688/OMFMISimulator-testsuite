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
setResultFile(model, "me_test1_res.mat")

initialize(model)
simulate(model)
terminate(model)

unload(model)

vars = {"test1.x", "test1.der(x)"}
for _,var in ipairs(vars) do
  if 1 == compareSimulationResults("me_test1_res.mat", "../ReferenceFiles/me_test1.mat", var, 1e-2, 1e-4) then
    print(var .. " is equal")
  else
    print(var .. " is not equal")
  end
end

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
-- test1.x is equal
-- test1.der(x) is equal
-- endResult
