'''
Created on Nov 6, 2016

@author: Vitoc
'''
from validator.valid import gradeValidatorException, gradeRepositoryException

class testGrade:

    def __init__(self, gradeCtrl):
        self.__gradeCtrl = gradeCtrl
        
    def __testAddFunction(self):
        self.__gradeCtrl.assignAssgiment(1,2)
        toVerify= self.__gradeCtrl.getById(1,2)
        assert(toVerify.assigmentId == 1)
        assert(toVerify.studentId == 2)
        assert(toVerify.grade == 0)
        try:
            self.__gradeCtrl.assignAssgiment(2,-1)
            assert(False)
        except gradeValidatorException:
            assert(True)
    
    def __testRemoveFunction(self):
        self.__gradeCtrl.assignAssgiment(2,2)
        self.__gradeCtrl.deleteGradeById(2,2)
        try:
            self.__gradeCtrl.deleteGradeById(2,2)
            assert(False)
        except gradeRepositoryException:
            assert(True)
    
    def run(self):
        self.__testAddFunction()
        self.__testRemoveFunction()