'''
Created on Dec 11, 2016

@author: Vitoc
'''
from repository.gradeRepository import gradeRepository

class gradeFileRepository:

    def __init__(self, filename,readEntity,writeEntity):
        '''
        Constructor
        '''
        gradeRepository.__init__(self)
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
                        self._grades[(entity.assigmentId,entity.studentId)]=entity
        except IOError:
            pass
        except:
            pass
        
    def __writeToFile(self):
        f = open(self.__filename,'w')
        for entity in self._grades.values():
            f.write(self.__writeEntity(entity)+"\n") 
        f.close()
    
    def addGrade(self,entity):
        gradeRepository.addGrade(self, entity)
        self.__writeToFile()
        
    def removeGradeById(self,ident):
        gradeRepository.removeGradeById(self, ident)
        self.__writeToFile()
        
    def updateGrade(self,entity):
        gradeRepository.updateGrade(self, entity)
        self.__writeToFile()
    
    def findById(self,toFind):
        return gradeRepository.findById(self, toFind)
    
    def getAll(self):
        return gradeRepository.getAll(self)
    
    def __add__(self,toAdd):
        self.addGrade(toAdd)
        
    def __radd__(self,toAdd):
        self.addGrade(toAdd)
        
    def __sub__(self,toRemove):
        if type(toRemove) is int:
            self.removeGradeById(toRemove)
                
    def __rsub__(self,toRemove):
        self.__sub__(toRemove)  
        
    def __getitem__(self,toFind):
        return self.findById(toFind)
    
    def __len__(self):
        return len(self._grades)
    
    def __str__(self):
        st = ""
        for x in self._grades.values():
            st += str(x)+"\n"
        return st
