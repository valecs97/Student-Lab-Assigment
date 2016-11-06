'''
Created on Nov 2, 2016

@author: Vitoc
'''

from domain.gradeDomain import gradeDomain
from validator.valid import gradeValidator

class gradeController:


    def __init__(self,repo):
        self.__repo = repo
        self.__validate = gradeValidator()
        
    '''
    Function that assign an assigment to a student
    
    input data:
    studentId - integer
    assigmentId - integer
    
    Raises gradeValidationException if :
    1.The assigment Id is a negative number (P.S the ui function has a exception if the object is not a number)
    1.The student Id is a negative number
    
    note :
    The program will not verify if the student has the assigment yet... it will just overwrite it
    In the next iteration a function will verify if the grade is different than 0 (0 means it is assigned but not given a grade)
    and if it is it will not overwrite it
    
    '''    
    
    def assignAssgiment(self,assigmentId,studentId):
        self.__validate.idsValidator(assigmentId,studentId)
        grade = gradeDomain(assigmentId,studentId,0)
        self.__repo + grade
        
        
    '''
    
    TO BE UPDATED IN THE FUTURE ITERATIONS
    
    def updateGrade(self,studentId,assigmentId,grade):
        grade = gradeDomain(assigmentId,studentId,grade)
        self.__validate.gradeValidator(grade)
        self.__repo.updateGrade(grade)
    '''
        
    '''
    Function that deletes a grade (or assigment to a student)
    
    input data:
    studentId - integer
    assigmentId - integer
    ''' 
        
    def deleteGradeById(self,assigmentId,studentId):
        (assigmentId,studentId) - self.__repo
        
    '''
    def deleteAssigment(self,studentId,assigmentId,grade):
        grade = gradeDomain(assigmentId,studentId,grade)
        self.__validate.gradeValidator(grade)
        self.__repo - grade
    '''
        
    '''
    Function that gets a grade (or assigment to a stundet) by the id:
    
    input data:
    studentId - integer
    assigmentId - integer
    
    output data:
    gradeDomain
    ''' 
        
    def getById(self,assigmentId,studentId):
        return self.__repo[(assigmentId,studentId)]
    
    '''
    Function that gets all grades (or assigment to a student) :
    

    output data:
    a list of assigments gradeDomain
    ''' 
    
    def getAll(self):
        return self.__repo.getAll()