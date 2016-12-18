'''
Created on Dec 11, 2016

@author: Vitoc
'''
from repository.studentRepository import studentRepository

class studentFileRepository:

    def __init__(self, filename,readEntity,writeEntity):
        '''
        Constructor
        '''
        studentRepository.__init__(self)
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
                        self._students[entity.studentId]=entity
        except IOError:
            pass
        except:
            pass
        
    def __writeToFile(self):
        f = open(self.__filename,'w')
        for entity in self._students.values():
            f.write(self.__writeEntity(entity)+"\n") 
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
