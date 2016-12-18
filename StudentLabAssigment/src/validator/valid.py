'''
Created on Nov 2, 2016

@author: Vitoc
'''

class studentRepositoryException(Exception):
    pass

class assigmentRepositoryException(Exception):
    pass

class gradeRepositoryException(Exception):
    pass

class studentValidatorException(Exception):
    pass

class gradeValidatorException(Exception):
    pass

class assigmentValidatorException(Exception):
    pass

class undoRedoValidatorException(Exception):
    pass

class studentValidator:
    '''
    Function that validates the studentDomain object
    
    input data : 
    toValidate - studentDomain
    
    Raises studentValidationException if :
    1.The id is not positive
    2.The name field is empty
    3.The group is not higher than 0
    '''
    def studentValidator(self,toValidate):
        errors=''
        if toValidate.studentId < 0 :
            errors+='The ID must be positive\n'
        if toValidate.name == '':
            errors+='The student name field can not be empty\n'
        if toValidate.group<1:
            errors+='The group must be positive\n'
        if len(errors)>0:
            raise studentValidatorException(errors)
        
        
class assigmentValidator:
    '''
    Function that validates the assigmentDomain object
    
    input data : 
    toValidate - assigmentDomain
    
    Raises assigmentValidationException if :
    1.The id is not positive
    2.The description field is empty
    3.If the date is not valid
    4.If the grade isnt between 1 and 10
    '''
    def assigmentValidator(self,toValidate):
        errors=''
        if toValidate.assigmentId < 0 :
            errors+='The ID must be positive\n'
        if toValidate.description == '':
            errors+='The description field can not be empty\n'
        '''
        To properly check if the deadline is a date
        '''
        if type(toValidate.deadline[0]) != int or type(toValidate.deadline[1]) != int or type(toValidate.deadline[2]) != int:
            errors+='The deadline must be a date'
        else:
            errors+=self.dateValidation(toValidate.deadline)
        if toValidate.grade<0 or toValidate.grade>10:
            errors+='The grade must be between 1 and 10\n'
        if len(errors)>0:
            raise assigmentValidatorException(errors)
        
    '''
    Function that validates the date
    
    input data :
    toValidate - list of 3 integers
    '''
        
    def dateValidation(self,toValidate):
        if toValidate[0]<1 or toValidate[0]>31 or toValidate[1]<1 or toValidate[1]>12 or toValidate[2]<0:
            return 'The date must be a valid type\n'
        import time
        todayTime = time.strftime("%d %m %Y")
        todayTime = todayTime.split(' ')
        todayTime = [int(todayTime[0]),int(todayTime[1]),int(todayTime[2])]
        if toValidate[2]<todayTime[2]:
            return 'The year must be higher or equal than the current date\n'
        if toValidate[2]==todayTime[2]:
            if toValidate[1]<todayTime[1]:
                return 'The month must be higher or equal than the current date\n'
        if toValidate[2]==todayTime[2] and toValidate[1]==todayTime[1]:
            if toValidate[0]<todayTime[0]:
                return 'The day must be higher or equal than the current date\n'
        if toValidate[2]%4==0 and toValidate[0]>29 and toValidate[1]==2:
            return 'February only got 29 days\n'
        if toValidate[2]%4!=0 and toValidate[0]>28 and toValidate[1]==2:
            return 'February only got 28 days\n'
        monthWith30Days = [4,6,9,11]
        if toValidate[1] in monthWith30Days:
            if toValidate[0]>30:
                return 'This month only got 30 days\n'
        return ''
        
class gradeValidator:
    '''
    Function that validates the grade ids
    '''
    def idsValidator(self,studentId,assigmentId):
        errors = ''
        if studentId < 0 :
            errors+='The student ID must be positive\n'
        if assigmentId < 0 :
            errors+='The assigment ID must be positive\n'
        if len(errors)>0:
            raise gradeValidatorException(errors)
            
    '''
    Function that validates the grade
    '''
    
    def gradeValidator(self,toValidate):
        errors=''
        if toValidate.studentId < 0 :
            errors+='The student ID must be positive\n'
        if toValidate.assigmentId < 0 :
            errors+='The assigment ID must be positive\n'
        '''
        to check assigment grade too
        '''
        if toValidate.grade<1 or toValidate.grade>10:
            errors+='The grade must be between 1 and 10\n'
        if len(errors)>0:
            raise gradeValidatorException(errors)