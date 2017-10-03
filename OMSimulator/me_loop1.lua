-- status: correct

setLogFile("omsllog.txt")

model = newModel()
setTempDirectory(".")

instantiateFMU(model, "../FMUs/me_loop1_A.fmu", "A")
instantiateFMU(model, "../FMUs/me_loop1_B.fmu", "B")
instantiateFMU(model, "../FMUs/cs_loop1_P.fmu", "P")

-- add connections
addConnection(model, "A.y", "B.u")
addConnection(model, "B.y", "A.u")
addConnection(model, "P.y", "A.p")
addConnection(model, "P.y", "B.p")

--name = "loop1"
--exportCompositeStructure(model, name)
--os.execute("dot -Gsplines=none " .. name .. ".dot | neato -n -Gsplines=ortho -Tpng -o" .. name .. ".png")

setResultFile(model, "me_loop1_res.mat")
setStopTime(model, 0.5)
setCommunicationInterval(model, 1e-2)
setTolerance(model, 1e-6)

describe(model)

initialize(model)
simulate(model)
terminate(model)

unload(model)

vars = {"A.y", "B.y"}
for _,var in ipairs(vars) do
  if 1 == compareSimulationResults("me_loop1_res.mat", "../ReferenceFiles/me_loop1_res.mat", var, 1e-4, 1e-2) then
    print(var .. " is equal")
  else
    print(var .. " is not equal")
  end
end

-- Result:
-- # FMU instances
-- P
--   - FMI 2.0 CS
--   - path: ../FMUs/cs_loop1_P.fmu
--   - GUID: {80806ada-692b-440a-98cb-507efc33c70b}
--   - tool: OpenModelica Compiler OMCompiler v1.13.0-dev.50+g23493d8
--   - input interface:
--   - output interface:
--     - output y
--   - parameters:
-- B
--   - FMI 2.0 ME (solver: euler)
--   - path: ../FMUs/me_loop1_B.fmu
--   - GUID: {1afc66ed-ff9c-403c-be0f-e49661ad8fcc}
--   - tool: OpenModelica Compiler OMCompiler v1.13.0-dev.50+g23493d8
--   - input interface:
--     - input p
--     - input u
--   - output interface:
--     - output y
--   - parameters:
-- A
--   - FMI 2.0 ME (solver: euler)
--   - path: ../FMUs/me_loop1_A.fmu
--   - GUID: {28101fc7-8911-4065-a1f6-563c4d62f97f}
--   - tool: OpenModelica Compiler OMCompiler v1.13.0-dev.50+g23493d8
--   - input interface:
--     - input p
--     - input u
--   - output interface:
--     - output y
--   - parameters:
--
-- # Simulation settings
--   - start time: 0
--   - stop time: 0.5
--   - tolerance: 1e-06
--   - communication interval: 0.01
--   - result file: me_loop1_res.mat
--
-- # Composite structure
-- ## Initialization
-- P.y -> B.p
-- P.y -> A.p
-- {B.y -> A.u; A.y -> B.u}
--
-- ## Simulation
-- P.y -> B.p
-- P.y -> A.p
-- {B.y -> A.u; A.y -> B.u}
--
-- stdout            | info    | The initialization finished successfully without homotopy method.
-- stdout            | info    | The initialization finished successfully without homotopy method.
-- stdout            | info    | The initialization finished successfully without homotopy method.
-- A.y is equal
-- B.y is equal
-- info:    2 warnings
-- info:    0 errors
-- info:    Logging information has been saved to "omsllog.txt"
-- endResult
