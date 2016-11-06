'''
Created on Nov 6, 2016

@author: Vitoc
'''
from validator.valid import assigmentValidatorException,\
    assigmentRepositoryException

class testAssigments:

    def __init__(self, assigmentCtrl):
        self.__assigmentCtrl = assigmentCtrl
        
    def __testAddFunction(self):
        self.__assigmentCtrl.addAssigment(1,'Test description',[15,12,2016],10)
        toVerify= self.__assigmentCtrl.getById(1)
        assert(toVerify.assigmentId == 1)
        assert(toVerify.description == 'Test description')
        assert(toVerify.deadline == [15,12,2016])
        assert(toVerify.grade == 10)
        try:
            self.__assigmentCtrl.addAssigment(2,'Test description',[15,12,2015],10)
            assert(False)
        except assigmentValidatorException:
            assert(True)
        try:
            self.__assigmentCtrl.addAssigment(1,'Test description',[15,12,2016],10)
            assert(False)
        except assigmentRepositoryException:
            assert(True)
    
    def __testRemoveFunction(self):
        self.__assigmentCtrl.addAssigment(2,'Test description',[15,12,2016],10)
        self.__assigmentCtrl.deleteAssigmentById(2)
        try:
            self.__assigmentCtrl.deleteAssigmentById(2)
            assert(False)
        except assigmentRepositoryException:
            assert(True)
    
    def __testUpdateFunction(self):
        assert(self.__assigmentCtrl.getById(1).description=='Test description')
        self.__assigmentCtrl.updateAssigment(1,'Test 2',[15,12,2016],10)
        try:
            assert(self.__assigmentCtrl.getById(1).description=='Test description')
            assert(False)
        except AssertionError:
            assert(True)
    
    def run(self):
        self.__testAddFunction()
        self.__testRemoveFunction()
        self.__testUpdateFunction()