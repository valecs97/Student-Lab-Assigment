'''
Created on Dec 11, 2016

@author: Vitoc
'''
from repository.studentRepository import studentRepository
import pickle

class studentPickleRepository:

    def __init__(self, filename):
        '''
        Constructor
        '''
        studentRepository.__init__(self)
        self.__filename = filename
        self.__readFromFile()
        
    def __readFromFile(self):
        for p in self.__readEffectivelyFromFile():
            studentRepository.addStudent(self, p)
            
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
        pickle.dump(studentRepository.getAll(self), f)
        f.close()
    
    def addStudent(self,entity):
        studentRepository.addStudent(self, entity)
        self.__writeToFile()
        
    def removeStudentById(self,ident):
        studentRepository.removeStudentById(self, ident)
        self.__writeToFile()
        
    def updateStudent(self,entity):
        studentRepository.updateStudent(self, entity)
        self.__writeToFile()
    
    def findById(self,toFind):
        return studentRepository.findById(self, toFind)
    
    def getAll(self):
        return studentRepository.getAll(self)
    
    def __add__(self,toAdd):
        self.addStudent(toAdd)
        
    def __radd__(self,toAdd):
        self.addstudent(toAdd)
        
    def __sub__(self,toRemove):
        if type(toRemove) is int:
            self.removeStudentById(toRemove)    
                
    def __rsub__(self,toRemove):
        self.__sub__(toRemove)  
        
    def __getitem__(self,toFind):
        return self.findById(toFind)
    
    def __len__(self):
        return len(self._students)
    
    def __str__(self):
        st = ""
        for x in self._students.values():
            st += str(x)+"\n"
        return st
