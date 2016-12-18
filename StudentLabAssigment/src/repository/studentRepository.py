'''
Created on Nov 2, 2016

@author: Vitoc
'''

from validator.valid import studentRepositoryException
from domain.studentDomain import studentDomain

class studentRepository:


    def __init__(self):
        self._students={}
    
    '''
    Function that adds the student to the repository
    
    input data :
    toAdd - studentDomain
    
    Raise studentRepositoryException if :
    1.The id already exists
    '''
    
    def addStudent(self,toAdd):
        if toAdd.studentId in self._students:
            raise studentRepositoryException('Invalid ID!')
        self._students[toAdd.studentId]=toAdd
    
    '''
    Function that updates the student in the repository
    
    input data :
    toUpdate - studentDomain
    
    Raise studentRepositoryException if :
    1.The id doesnt exist
    '''
    
    def updateStudent(self,toUpdate):
        if toUpdate.studentId not in self._students:
            raise studentRepositoryException('Invalid ID!')
        self._students[toUpdate.studentId]=toUpdate
    ''' 
    def removeStudent(self,toRemove):
        if toRemove.studentId not in self._students:
            raise studentRepositoryException('Invalid ID!')
        del self._students[toRemove.studentId]
    '''
        
    '''
    Function that removes the student from the repository
    
    input data :
    toDelete - integer
    
    Raise studentRepositoryException if :
    1.The id doesnt exist
    '''
    
    def removeStudentById(self,toRemove):
        if toRemove not in self._students:
            raise studentRepositoryException('Invalid ID!')
        del self._students[toRemove]
    
    '''
    Function that finds an student in the repository
    
    input data :
    toFind - integer
    
    output data :
    studentDomain
    
    Raise studentRepositoryException if :
    1.The id doesnt exist
    '''
    
    def findById(self,toFind):
        if toFind not in self._students:
            raise studentRepositoryException('Invalid ID!')
        return self._students[toFind]
        
    '''
    Function that removes the student from the repository
    
    input data :
    toDelete - studentDomain
    
    output data:
    a list of studentDomain
    
    Raise studentRepositoryException if :
    1.The id doesnt exist
    '''   
    
    def getAll(self):
        l=[]
        for i in self._students.values():
            l.append(i)
        return l
    
    '''
    Function that helps the controller to call the function easier
    '''
    
    def __add__(self,toAdd):
        self.addStudent(toAdd)
        
    def __radd__(self,toAdd):
        self.addstudent(toAdd)
        
    def __sub__(self,toRemove):
        if type(toRemove) is int:
            self.removeStudentById(toRemove)    
        if type(toRemove) is studentDomain:
            self.removeStudent(toRemove)
                
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