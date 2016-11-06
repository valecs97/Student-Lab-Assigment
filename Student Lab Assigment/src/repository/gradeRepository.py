'''
Created on Nov 2, 2016

@author: Vitoc
'''

from validator.valid import gradeRepositoryException
#from domain.gradeDomain import gradeDomain

class gradeRepository:


    def __init__(self):
        self.__grades={}
        
    '''
    Function that adds a grade to a repository
    
    input data :
    toAdd - gradeDomain
    
    No raises will occur if the id already exists , it will just overwrite it
    Future modification will be implemented in iteration 2
    '''
        
    def addGrade(self,toAdd):
        self.__grades[(toAdd.assigmentId,toAdd.studentId)]=toAdd
    
    '''
    TO BE UPDATED ITERATION
    
    def updateGrade(self,toUpdate):
        if [toUpdate.assigmentId,toUpdate.studentId] not in self.__grades:
            raise gradeRepositoryException('Invalid ID!')
        if gradeDomain.get_grade(self.__grade[[toUpdate.assigmentId,toUpdate.studentId]])==0:
            raise gradeRepositoryException('Grades can not be changed')
        self.__grade[[toUpdate.assigmentId,toUpdate.studentId]]=toUpdate
        
    def removeGrade(self,toRemove):
        if [toRemove.assigmentId,toRemove.studentId] not in self.__grades:
            raise gradeRepositoryException('Invalid ID!')
        del self.__grades[[toRemove.assigmentId,toRemove.studentId]]
    '''
        
    '''
    Function that removes a grade
    TO BE UPDATED IN THE NEXT ITERATION
    '''
        
    def removeGradeById(self,toRemove):
        if toRemove not in self.__grades:
            raise gradeRepositoryException('Invalid ID!')
        del self.__grades[toRemove]
    
    '''
    Function that finds a grade
    TO BE UPDATED IN THE NEXT ITERATION
    '''
    
    def findById(self,toFind):
        if toFind not in self.__grades:
            raise gradeRepositoryException('Invalid ID!')
        return self.__grades[toFind]
    
    '''
    Function that gets all the grades
    TO BE UPDATED IN THE NEXT ITERATION
    '''
    
    def getAll(self):
        l=[]
        for i in self.__grades.values():
            l.append(i)
        return l
        
    '''
    Function that helps the controller to call the function easier
    '''
        
    def __add__(self,toAdd):
        self.addGrade(toAdd)
        
    def __radd__(self,toAdd):
        self.addGrade(toAdd)
        
    '''
    TO BE UPDATE IN THE NEXT ITERATION
    '''
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
        return len(self.__grades)
    
    def __str__(self):
        st = ""
        for x in self.__grades.values():
            st += str(x)+"\n"
        return st