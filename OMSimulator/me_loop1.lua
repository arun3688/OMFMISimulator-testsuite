-- status: correct

setLogFile("omsllog.txt")

model = newModel()
setTempDirectory(".")

instantiateFMU(model, "../FMUs/me.loop1.A.fmu", "A")
instantiateFMU(model, "../FMUs/me.loop1.B.fmu", "B")
instantiateFMU(model, "../FMUs/cs.loop1.P.fmu", "P")

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
  if 1 == compareSimulationResults("me_loop1_res.mat", "../ReferenceFiles/me_loop1.mat", var, 1e-4, 1e-2) then
    print(var .. " is equal")
  else
    print(var .. " is not equal")
  end
end

-- Result:
-- # FMU instances
-- P
--   - FMI 2.0 CS
--   - path: ../FMUs/cs.loop1.P.fmu
--   - GUID: {4cca3b30-6b93-42f0-924c-1ab12147a132}
--   - tool: OpenModelica Compiler OMCompiler v1.13.0-dev.70+g702501a
--   - input interface:
--   - output interface:
--     - output y
--   - parameters:
-- B
--   - FMI 2.0 ME (solver: euler)
--   - path: ../FMUs/me.loop1.B.fmu
--   - GUID: {709cce92-f6f9-45a5-a044-8d3c7fd182d5}
--   - tool: OpenModelica Compiler OMCompiler v1.13.0-dev.70+g702501a
--   - input interface:
--     - input p
--     - input u
--   - output interface:
--     - output y
--   - parameters:
-- A
--   - FMI 2.0 ME (solver: euler)
--   - path: ../FMUs/me.loop1.A.fmu
--   - GUID: {4d5c58f9-203c-4148-ad40-6e3a7593a3f4}
--   - tool: OpenModelica Compiler OMCompiler v1.13.0-dev.70+g702501a
--   - input interface:
--     - input p
--     - input u
--   - output interface:
--     - output y
--   - parameters:
--
-- # Lookup tables
--
-- # Simulation settings
--   - start time: 0
--   - stop time: 0.5
--   - tolerance: 1e-06
--   - communication interval: 0.01
--   - result file: me_loop1_res.mat
--
-- # Composite structure
-- ## External inputs
--
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
