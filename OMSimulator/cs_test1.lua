-- status: correct

version = getVersion()
-- print(version)

model = newModel()
setTempDirectory(".")

instantiateFMU(model, "../FMUs/cs_test1.fmu", "test1")
describe(model)

setStopTime(model, 2.1)
setTolerance(model, 1e-5)
setResultFile(model, "cs_test1_res.mat")

initialize(model)
simulate(model)
terminate(model)

unload(model)

vars = {"test1.x"}
for _,var in ipairs(vars) do
  if 1 == compareSimulationResults("cs_test1_res.mat", "../ReferenceFiles/cs_test1.mat", var, 1e-2, 1e-4) then
    print(var .. " is equal")
  else
    print(var .. " is not equal")
  end
end

-- Result:
-- # FMU instances
-- test1
--   - FMI 2.0 CS
--   - path: ../FMUs/cs_test1.fmu
--   - GUID: {e72ab90f-3c54-4c60-a423-177dbaddd14c}
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
-- endResult
