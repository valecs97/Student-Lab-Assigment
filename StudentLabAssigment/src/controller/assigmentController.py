'''
Created on Nov 2, 2016

@author: Vitoc
'''
from validator.valid import assigmentValidator
from domain.assigmentDomain import assigmentDomain

class assigmentController:


    def __init__(self,repo):
        self.__repo = repo
        self.__validate = assigmentValidator()
       
    '''
    Function which adds an assigment in the repository
    
    input data :
    assigmentId - integer
    description - string
    deadline - date <dd.mm.yyyy>
    grade - integer between 1 and 10
    
    Raises :
    assigmentValidationException if :
    1.The assigment Id is a negative number (P.S the ui function has a exception if the object is not a number)
    2.The description is empty
    3.The deadline is not a date (a special function verifies if the deadline is a valid date , if it is in the future of the current date and so on...)
    4.The grade is not between 1 and 10
    
    '''
    def addAssigment(self,assigmentId,description,deadline,grade):
        assigment = assigmentDomain(assigmentId,description,deadline,grade)
        self.__validate.assigmentValidator(assigment)
        self.__repo + assigment
        
    '''
    Function that updates an assigment in the repository
    
    input data :
    assigmentId - integer
    description - string
    deadline - date <dd.mm.yyyy>
    grade - integer between 1 and 10
    
    Raises :
    assigmentValidationException if :
    1.The assigment Id is a negative number (P.S the ui function has a exception if the object is not a number)
    2.The description is empty
    3.The deadline is not a date (a special function verifies if the deadline is a valid date , if it is in the future of the current date and so on...)
    4.The grade is not between 1 and 10
    '''
    
    def updateAssigment(self,assigmentId,description,deadline,grade):
        assigment = assigmentDomain(assigmentId,description,deadline,grade)
        self.__validate.assigmentValidator(assigment)
        self.__repo.updateAssigment(assigment)
        
    '''
    Function that deletes an assigment in the repository
    
    input data :
    assigmentId - integer
    '''   
         
    def deleteAssigmentById(self,assigmentId):
        assigmentId - self.__repo
    
    '''
    def deleteAssigment(self,assigmentId,description,deadline,grade):
        assigment = assigmentDomain(assigmentId,description,deadline,grade)
        self.__validate.assigmentValidator(assigment)
        self.__repo - assigment
    '''
        
        
    '''
    Function that gets an assigment by the Id :
    
    input data :
    assigmentId - integer
    
    output data :
    assigmentDomain
    '''
    def getById(self,assigmentId):
        return self.__repo[assigmentId]
    
    def getLen(self):
        return len(self.__repo)
        
    '''
    Function that gets all the assigments
    
    output data :
    a list of assigmentDomain
    '''
    def getAll(self):
        return self.__repo.getAll()