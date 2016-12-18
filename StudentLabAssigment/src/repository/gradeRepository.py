'''
Created on Nov 2, 2016

@author: Vitoc
'''

from validator.valid import gradeRepositoryException
#from domain.gradeDomain import gradeDomain

class gradeRepository:


    def __init__(self):
        self._grades={}
        
    '''
    Function that adds a grade to a repository
    
    input data :
    toAdd - gradeDomain
    
    No raises will occur if the id already exists , it will just overwrite it
    Future modification will be implemented in iteration 2
    '''
        
    def addGrade(self,toAdd):
        if (toAdd.assigmentId,toAdd.studentId) in self._grades:
            return
        self._grades[(toAdd.assigmentId,toAdd.studentId)]=toAdd
    
    def updateGrade(self,toUpdate):
        if (toUpdate.assigmentId,toUpdate.studentId) not in self._grades:
            raise gradeRepositoryException('Invalid ID!')
        self._grades[(toUpdate.assigmentId,toUpdate.studentId)]=toUpdate
        
    '''
    def removeGrade(self,toRemove):
        if [toRemove.assigmentId,toRemove.studentId] not in self._grades:
            raise gradeRepositoryException('Invalid ID!')
        del self._grades[[toRemove.assigmentId,toRemove.studentId]]
    '''
        
    '''
    Function that removes a grade
    
    input data:
    toRemove-touple of 2 integers
    
    raises gradeRepositoryException if the id doesnt exists
    '''
        
    def removeGradeById(self,toRemove):
        if toRemove not in self._grades:
            raise gradeRepositoryException('Invalid ID!')
        del self._grades[toRemove]
    
    '''
    Function that finds a grade by id
    
    input data:
    toFind - touple of 2 integers
    
    raises gradeRepositoryException if the id doesnt exists
    '''
    
    def findById(self,toFind):
        if toFind not in self._grades:
            raise gradeRepositoryException('Invalid ID!')
        return self._grades[toFind]
    
    '''
    Function that gets all the grades
    
    output data:
    a list of gradeDomain
    '''
    
    def getAll(self):
        l=[]
        for i in self._grades.values():
            l.append(i)
        return l
        
    '''
    Function that helps the controller to call the function easier
    '''
        
    def __add__(self,toAdd):
        self.addGrade(toAdd)
        
    def __radd__(self,toAdd):
        self.addGrade(toAdd)
        

    def __sub__(self,toRemove):
        if type(toRemove[0]) is int and type(toRemove[1]) is int:
            self.removeGradeById(toRemove)
        '''  
        if type(toRemove) is gradeDomain:
            self.removeGrade(toRemove)
        '''
                
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