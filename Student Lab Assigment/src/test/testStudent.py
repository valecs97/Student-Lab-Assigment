'''
Created on Nov 6, 2016

@author: Vitoc
'''

from validator.valid import studentValidatorException,studentRepositoryException

class testStudent:
    


    def __init__(self, studentCtrl):
        self.__studentCtrl = studentCtrl
        
    def __testAddFunction(self):
        self.__studentCtrl.addStudent(1,'Test name',916)
        toVerify= self.__studentCtrl.getById(1)
        assert(toVerify.studentId == 1)
        assert(toVerify.name == 'Test name')
        assert(toVerify.group == 916)
        try:
            self.__studentCtrl.addStudent(2,'Test name',0)
            assert(False)
        except studentValidatorException:
            assert(True)
        try:
            self.__studentCtrl.addStudent(1,'Test name',916)
            assert(False)
        except studentRepositoryException:
            assert(True)
    
    def __testRemoveFunction(self):
        self.__studentCtrl.addStudent(2,'Test name',916)
        self.__studentCtrl.deleteStudentById(2)
        try:
            self.__studentCtrl.deleteStudentById(2)
            assert(False)
        except studentRepositoryException:
            assert(True)
    
    def __testUpdateFunction(self):
        assert(self.__studentCtrl.getById(1).name=='Test name')
        self.__studentCtrl.updateStudent(1,'Test name 2',916)
        try:
            assert(self.__studentCtrl.getById(1).name=='Test name')
            assert(False)
        except AssertionError:
            assert(True)
        
    def run(self):
        self.__testAddFunction()
        self.__testRemoveFunction()
        self.__testUpdateFunction()