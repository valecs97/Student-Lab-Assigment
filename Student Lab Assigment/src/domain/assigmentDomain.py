'''
Created on Nov 2, 2016

@author: Vitoc
'''

class assigmentDomain:

    '''
    A assigment domain which stores the id , description , deadline and grade 
    There are also getters and setters for each object apart
    '''

    def __init__(self,assigmentId,description,deadline,grade):
        self.__assigmentId=assigmentId
        self.__description=description
        self.__deadline=deadline
        self.__grade=grade

    def get_assigment_id(self):
        return self.__assigmentId


    def get_description(self):
        return self.__description


    def get_deadline(self):
        return self.__deadline


    def get_grade(self):
        return self.__grade


    def set_assigment_id(self, value):
        self.__assigmentId = value


    def set_description(self, value):
        self.__description = value


    def set_deadline(self, value):
        self.__deadline = value


    def set_grade(self, value):
        self.__grade = value


    def del_assigment_id(self):
        del self.__assigmentId


    def del_description(self):
        del self.__description


    def del_deadline(self):
        del self.__deadline


    def del_grade(self):
        del self.__grade
        
    '''
    To check if the date is a number or not
    '''
    def __str__(self):
        return str(self.__assigmentId) + ' ' +self.__description + ' ' + str(self.__deadline[0])+'.'+str(self.__deadline[1])+'.'+str(self.__deadline[2]) + ' ' + str(self.__grade)

    assigmentId = property(get_assigment_id, set_assigment_id, del_assigment_id, "assigmentId's docstring")
    description = property(get_description, set_description, del_description, "description's docstring")
    deadline = property(get_deadline, set_deadline, del_deadline, "deadline's docstring")
    grade = property(get_grade, set_grade, del_grade, "grade's docstring")
        
    
        