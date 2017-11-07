from ctypes import cdll
import ctypes,sys

class OMSimulatorPython:
     def __init__(self):
         if (sys.platform == 'win32'):
            self.obj=cdll.LoadLibrary("../../install/lib/OMSimulatorPython.dll")
         else:
            self.obj=cdll.LoadLibrary("../../install/lib/libOMSimulatorPython.so")
         self.setCtypesArguments()
         self.setResultTypes()
      
     def setResultTypes(self):
         self.obj.newModel.restype = ctypes.c_void_p
         self.obj.loadModel.restype = ctypes.c_void_p
         self.obj.getVersion.restype = ctypes.c_char_p
         self.obj.getBoolean.restype = ctypes.c_int
         self.obj.getInteger.restype = ctypes.c_int
         self.obj.getReal.restype = ctypes.c_double
         self.obj.compareSimulationResults.restype = ctypes.c_int
         self.obj.getNumberOfInterfaces.restype = ctypes.c_int
         self.obj.getInterfaceName.restype = ctypes.c_char_p       
         self.obj.getInterfaceVariable.restype = ctypes.c_char_p
         self.obj.getCurrentTime.restype = ctypes.c_double

     def setCtypesArguments(self):
         self.obj.instantiateFMU.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
         self.obj.addConnection.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
         self.obj.describe.argtypes = [ctypes.c_void_p]
         self.obj.initialize.argtypes = [ctypes.c_void_p]
         self.obj.terminate.argtypes = [ctypes.c_void_p]
         self.obj.unload.argtypes = [ctypes.c_void_p]
         self.obj.reset.argtypes = [ctypes.c_void_p]
         self.obj.simulate.argtypes = [ctypes.c_void_p]
         self.obj.loadModel.argtypes = [ctypes.c_char_p]
         self.obj.importXML.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
         self.obj.exportXML.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
         self.obj.exportDependencyGraph.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
         self.obj.exportCompositeStructure.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
         self.obj.getCurrentTime.argtypes = [ctypes.c_void_p]       
         self.obj.stepUntil.argtypes = [ctypes.c_void_p, ctypes.c_double]
         self.obj.doSteps.argtypes = [ctypes.c_void_p, ctypes.c_int]
         self.obj.getBoolean.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
         self.obj.getInteger.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
         self.obj.getReal.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
         self.obj.setBoolean.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
         self.obj.setInteger.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
         self.obj.setReal.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_double]
         self.obj.setStartTime.argtypes = [ctypes.c_void_p,ctypes.c_double]
         self.obj.setStopTime.argtypes = [ctypes.c_void_p,ctypes.c_double]
         self.obj.setTolerance.argtypes = [ctypes.c_void_p,ctypes.c_double]
         self.obj.setCommunicationInterval.argtypes = [ctypes.c_void_p,ctypes.c_double]
         self.obj.setResultFile.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
         self.obj.setTempDirectory.argtypes = [ctypes.c_char_p]
         self.obj.setSolverMethod.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
         self.obj.setLogFile.argtypes = [ctypes.c_char_p]
         self.obj.compareSimulationResults.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double,ctypes.c_double]
         self.obj.setVariableFilter.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
         self.obj.getNumberOfInterfaces.argtypes = [ctypes.c_void_p]
         self.obj.getInterfaceCausality.argtypes = [ctypes.c_void_p, ctypes.c_int]
         self.obj.getInterfaceName.argtypes = [ctypes.c_void_p, ctypes.c_int]
         self.obj.getInterfaceVariable.argtypes = [ctypes.c_void_p, ctypes.c_int]
         self.obj.setWorkingDirectory.argtypes =[ctypes.c_char_p]         

     def newModel(self):
         return self.obj.newModel()
     
     def loadModel(self,filename):
         return self.obj.loadModel(filename)
         
     def instantiateFMU(self, model, filename, instanceName):      
         self.obj.instantiateFMU(model, filename, instanceName)         
      
     def instantiateTable(self, model, filename, instanceName):      
         self.obj.instantiateTable(model, filename, instanceName)       
         
     def describe(self, model):
         self.obj.describe(model)  
  
     def initialize(self,model):
         self.obj.initialize(model) 
         
     def terminate(self,model):
         self.obj.terminate(model)             
      
     def unload(self,model):
         self.obj.unload(model)
     
     def reset(self,model):
         self.obj.reset(model)              
 
     def simulate(self,model):
         self.obj.simulate(model)   
         
     def addConnection(self, model, fromconnection, toconnection):
         self.obj.addConnection(model,fromconnection,toconnection)
      
     def importXML(self, model, filename):
         self.obj.importXML(model,filename)

     def exportXML(self, model, filename):
         self.obj.exportXML(model,filename)
 
     def exportDependencyGraph(self, model, filename):
         self.obj.exportDependencyGraph(model,filename)

     def exportCompositeStructure(self, model, filename):
         self.obj.exportCompositeStructure(model,filename)
     
     def getCurrentTime(self, model):
         return self.obj.getCurrentTime(model)
     
     def doSteps(self, model, numberOfSteps):
         self.obj.doSteps(model,numberOfSteps)
     
     def stepUntil(self, model, timeValue):
         self.obj.stepUntil(model,timeValue)
      
     def getVersion(self):
         return self.obj.getVersion()
         
     def getBoolean(self, model, var):
         return self.obj.getBoolean(model,var)

     def getInteger(self, model, var):
         return self.obj.getInteger(model,var) 
     
     def getReal(self, model, var):
         return self.obj.getReal(model,var)
         
     def setBoolean(self, model, var, value):
         self.obj.setBoolean(model,var,value)

     def setInteger(self, model, var, value):
         self.obj.setInteger(model,var,value)
      
     def setReal(self, model, var, value):
         self.obj.setReal(model,var,value)      
        
     def setResultFile(self, model, filename):
         self.obj.setResultFile(model,filename)

     def setTempDirectory(self, filename):
        self.obj.setTempDirectory(filename)

     def setWorkingDirectory(self, path):
        self.obj.setWorkingDirectory(path)
    
     def setStartTime(self, model, startTime):
        self.obj.setStartTime(model, startTime)

     def setStopTime(self, model, stopTime):
        self.obj.setStopTime(model, stopTime)
        
     def setTolerance(self, model, tolerance):
        self.obj.setTolerance(model, tolerance)
        
     def setCommunicationInterval(self, model, CommunicationInterval):
        self.obj.setCommunicationInterval(model, CommunicationInterval)
        
     def setSolverMethod(self, model, instanceName, method):
        self.obj.setSolverMethod(model, instanceName, method)

     def setLogFile(self, filename):
        self.obj.setLogFile(filename)

     def compareSimulationResults(self, filenameA, filenameB, var, relTol, absTol):
        return self.obj.compareSimulationResults(filenameA, filenameB, var, relTol, absTol)

     def setVariableFilter(self, model, instanceFilter, variableFilter):
        self.obj.setVariableFilter(model, instanceFilter, variableFilter)
   
     def getNumberOfInterfaces(self, model):
        return self.obj.getNumberOfInterfaces(model)
      
     def getInterfaceCausality(self, model, idx):
        self.obj.getInterfaceCausality(model, idx)
     
     def getInterfaceName(self, model, idx):
        return self.obj.getInterfaceName(model, idx)

     def getInterfaceVariable(self, model, idx):
        return self.obj.getInterfaceVariable(model, idx)

