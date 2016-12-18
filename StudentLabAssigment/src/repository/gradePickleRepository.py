'''
Created on Dec 11, 2016

@author: Vitoc
'''
from repository.gradeRepository import gradeRepository
import pickle

class gradePickleRepository:

    def __init__(self, filename):
        '''
        Constructor
        '''
        gradeRepository.__init__(self)
        self.__filename = filename
        self.__readFromFile()
        
    def __readFromFile(self):
        for p in self.__readEffectivelyFromFile():
            gradeRepository.addGrade(self, p)
            
    def __readEffectivelyFromFile(self):
        result = []
        try:
            f = open(self.__filename, "rb")
            return pickle.load(f)
        except EOFError:
            return []
        except IOError:
            pass
        return result
        
    def __writeToFile(self):
        f = open(self.__filename, "wb")
        pickle.dump(gradeRepository.getAll(self), f)
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
