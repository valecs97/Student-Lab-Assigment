'''
Created on Nov 2, 2016

@author: Vitoc
'''

from validator.valid import studentValidator
from domain.studentDomain import studentDomain

class studentController:


    def __init__(self,repo):
        self.__repo = repo
        self.__validate = studentValidator()
       
    '''
    Function which adds a student in the repository
    
    input data :
    studentId - integer
    name - string
    grade - integer between 1 and 10
    
    Raise studentValidationException if :
    1.The student Id is a negative number (P.S the ui function has a exception if the object is not a number)
    2.The name is empty
    3.The group is a negative number or 0
    
    '''
    
    def addStudent(self,studentId,name,group):
        student = studentDomain(studentId,name,group)
        self.__validate.studentValidator(student)
        self.__repo + student
        
    '''
    Function which updates a student in the repository
    
    input data :
    studentId - integer
    name - string
    grade - integer between 1 and 10
    
    Raise studentValidationException if :
    1.The student Id is a negative number (P.S the ui function has a exception if the object is not a number)
    2.The name is empty
    3.The group is a negative number or 0
    
    '''
        
    def updateStudent(self,studentId,name,group):
        student = studentDomain(studentId,name,group)
        self.__validate.studentValidator(student)
        self.__repo.updateStudent(student)
        
    '''
    Function which removes a student in the repository
    
    input data :
    studentId - integer
    '''
        
    def deleteStudentById(self,studentId):
        studentId - self.__repo
    '''
    def deleteStudent(self,studentId,name,group):
        student = studentDomain(studentId,name,group)
        self.__validate.studentValidator(student)
        self.__repo - student
    '''
        
    '''
    Function gets a student from the repository
    
    input data :
    studentId - integer
    
    output data :
    studentDomain
    '''
    
    def getById(self,studentId):
        return self.__repo[studentId]
    
    def getLen(self):
        return len(self.__repo)
        
    '''
    Function that gets all the students
    
    output data :
    a list of studentDomain
    '''
        
    def getAll(self):
        return self.__repo.getAll()