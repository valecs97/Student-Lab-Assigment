'''
Created on Dec 11, 2016

@author: Vitoc
'''
from repository.assigmentRepository import assigmentRepository

class assigmentFileRepository:

    def __init__(self, filename,readEntity,writeEntity):
        '''
        Constructor
        '''
        assigmentRepository.__init__(self)
        self.__filename = filename
        self.__readEntity = readEntity
        self.__writeEntity = writeEntity
        self.__readFromFile()
        
    def __readFromFile(self):
        try:
            with open(self.__filename) as f:
                content = f.readlines()
                for line in content:
                    if line !="\n":
                        entity = self.__readEntity(line)
                        self._assigments[entity.assigmentId]=entity
        except IOError:
            pass
        except:
            pass
        
    def __writeToFile(self):
        f = open(self.__filename,'w')
        for entity in self._assigments.values():
            f.write(self.__writeEntity(entity)+"\n") 
        f.close()
    
    def addAssigment(self,entity):
        assigmentRepository.addAssigment(self, entity)
        self.__writeToFile()
        
    def removeAssigmentById(self,ident):
        assigmentRepository.removeAssigmentById(self, ident)
        self.__writeToFile()
        
    def updateAssigment(self,entity):
        assigmentRepository.updateAssigment(self, entity)
        self.__writeToFile()
    
    def findById(self,toFind):
        return assigmentRepository.findById(self, toFind)
    
    def getAll(self):
        return assigmentRepository.getAll(self)
    
    def __add__(self,toAdd):
        self.addAssigment(toAdd)
        
    def __radd__(self,toAdd):
        self.addAssigment(toAdd)
        
    def __sub__(self,toRemove):
        if type(toRemove) is int:
            self.removeAssigmentById(toRemove)    
                
    def __rsub__(self,toRemove):
        self.__sub__(toRemove)  
        
    def __getitem__(self,toFind):
        return self.findById(toFind)     
    
    def __len__(self):
        return len(self._assigments)
    
    def __str__(self):
        st = ""
        for x in self._assigments.values():
            st += str(x)+"\n"
        return st
