'''
Created on Nov 2, 2016

@author: Vitoc
'''

class gradeDomain:

    '''
    A grade domain which stores the studentId , assigmentId and the grade 
    There are also getters and setters for each object apart
    '''

    def __init__(self,assigmentId,studentId,grade):
        self.__assigmentId=assigmentId
        self.__studentId=studentId
        self.__grade=grade

    def get_assigment_id(self):
        return self.__assigmentId


    def get_student_id(self):
        return self.__studentId


    def get_grade(self):
        return self.__grade


    def set_assigment_id(self, value):
        self.__assigmentId = value


    def set_student_id(self, value):
        self.__studentId = value


    def set_grade(self, value):
        self.__grade = value


    def del_assigment_id(self):
        del self.__assigmentId


    def del_student_id(self):
        del self.__studentId


    def del_grade(self):
        del self.__grade

    def __str__(self):
        return str(self.__assigmentId) + ' ' + str(self.__studentId) + ' ' +str(self.__grade)
    assigmentId = property(get_assigment_id, set_assigment_id, del_assigment_id, "assigmentId's docstring")
    studentId = property(get_student_id, set_student_id, del_student_id, "studentId's docstring")
    grade = property(get_grade, set_grade, del_grade, "grade's docstring")
        
    
        