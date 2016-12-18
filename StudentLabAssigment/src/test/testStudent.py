'''
Created on Nov 6, 2016

@author: Vitoc
'''

from validator.valid import studentValidatorException,studentRepositoryException
from domain.studentDomain import studentDomain
import unittest
from repository.studentRepository import studentRepository
from controller.studentController import studentController

class testStudent(unittest.TestCase):

    def setUp(self):
        self.__studentRepo = studentRepository()
        self.__studentCtrl = studentController(self.__studentRepo)
        unittest.TestCase.setUp(self)
        

    def tearDown(self):
        del self.__studentRepo
        del self.__studentCtrl
        unittest.TestCase.tearDown(self)
        
    def testAddFunction(self):
        self.__studentCtrl.addStudent(1,'Test name',916)
        toVerify= self.__studentCtrl.getById(1)
        assert(toVerify.studentId == 1)
        assert(toVerify.name == 'Test name')
        assert(toVerify.group == 916)
        self.__studentCtrl.getAll()
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
    
    def testRemoveFunction(self):
        self.__studentCtrl.addStudent(2,'Test name',916)
        self.__studentCtrl.deleteStudentById(2)
        try:
            self.__studentCtrl.deleteStudentById(2)
            assert(False)
        except studentRepositoryException:
            assert(True)
    
    def testUpdateFunction(self):
        self.__studentCtrl.addStudent(1,'Test name',916)
        assert(self.__studentCtrl.getById(1).name=='Test name')
        self.__studentCtrl.updateStudent(1,'Test name 2',916)
        try:
            assert(self.__studentCtrl.getById(1).name=='Test name')
            assert(False)
        except AssertionError:
            assert(True)
    
    def testStutdentValidator(self):
        with self.assertRaises(studentValidatorException):
            self.__studentCtrl.addStudent(-1, '', 0)
    
    def testDomain(self):
        testObject = studentDomain(123,'Test Testovici',916)
        assert(testObject.studentId == 123)
        assert(testObject.name == 'Test Testovici')
        assert(testObject.group == 916)
        assert(str(testObject) == '123 Test Testovici 916')
        del testObject.studentId
        del testObject.name
        del testObject.group
        testObject.studentId=1
        testObject.name='Name test'
        testObject.group=917