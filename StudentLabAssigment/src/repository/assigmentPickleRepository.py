'''
Created on Dec 11, 2016

@author: Vitoc
'''
from repository.assigmentRepository import assigmentRepository
import pickle

class assigmentPickleRepository:

    def __init__(self, filename):
        '''
        Constructor
        '''
        assigmentRepository.__init__(self)
        self.__filename = filename
        self.__readFromFile()
        
    def __readFromFile(self):
        for p in self.__readEffectivelyFromFile():
            assigmentRepository.addAssigment(self, p)
            
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
        pickle.dump(assigmentRepository.getAll(self), f)
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