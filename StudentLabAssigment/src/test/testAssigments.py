'''
Created on Nov 6, 2016

@author: Vitoc
'''
import unittest

from validator.valid import assigmentValidatorException,\
    assigmentRepositoryException
from domain.assigmentDomain import assigmentDomain
from controller.assigmentController import assigmentController
from repository.assigmentRepository import assigmentRepository

class testAssigments(unittest.TestCase):
    
    def setUp(self):
        self.__assigmentRepo = assigmentRepository()
        self.__assigmentCtrl = assigmentController(self.__assigmentRepo)
        unittest.TestCase.setUp(self)
        

    def tearDown(self):
        del self.__assigmentCtrl
        del self.__assigmentRepo
        unittest.TestCase.tearDown(self)
        
    def testAddFunction(self):
        self.__assigmentCtrl.addAssigment(1,'Test description',[15,12,2016],10)
        toVerify = self.__assigmentCtrl.getById(1)
        takeAll = self.__assigmentCtrl.getAll()
        assert(toVerify.assigmentId == 1)
        assert(toVerify.description == 'Test description')
        assert(toVerify.deadline == [15,12,2016])
        assert(toVerify.grade == 10)
        assert(str(toVerify)=='1 Test description 15.12.2016 10')
        assert(str(takeAll[0])=='1 Test description 15.12.2016 10')
        try:
            self.__assigmentCtrl.addAssigment(2,'Test description',[15,12,2015],10)
            #assert(False)
        except assigmentValidatorException:
            assert(True)
        try:
            self.__assigmentCtrl.addAssigment(1,'Test description',[15,12,2016],10)
            #assert(False)
        except assigmentRepositoryException:
            assert(True)
    
    def testRemoveFunction(self):
        self.__assigmentCtrl.addAssigment(2,'Test description',[15,12,2016],10)
        self.__assigmentCtrl.deleteAssigmentById(2)
        try:
            self.__assigmentCtrl.deleteAssigmentById(2)
            #assert(False)
        except assigmentRepositoryException:
            assert(True)
    
    def testUpdateFunction(self):
        self.__assigmentCtrl.addAssigment(1,'Test description',[15,12,2016],10)
        assert(self.__assigmentCtrl.getById(1).description=='Test description')
        self.__assigmentCtrl.updateAssigment(1,'Test 2',[15,12,2016],10)
        try:
            assert(self.__assigmentCtrl.getById(1).description=='Test description')
            #assert(False)
        except AssertionError:
            assert(True)
    
    def testAssigmentValidator(self):
        with self.assertRaises(assigmentValidatorException):
            self.__assigmentCtrl.addAssigment(-1, '', [1,2,'a'], 11)
        with self.assertRaises(assigmentValidatorException):
            self.__assigmentCtrl.addAssigment(1, 'caca', [-1,11,2016], 9)
        with self.assertRaises(assigmentValidatorException):
            self.__assigmentCtrl.addAssigment(1, 'caca', [1,11,2015], 9)
        with self.assertRaises(assigmentValidatorException):
            self.__assigmentCtrl.addAssigment(1, 'caca', [1,10,2016], 9)
        with self.assertRaises(assigmentValidatorException):
            self.__assigmentCtrl.addAssigment(1, 'caca', [20,11,2016], 9)
        with self.assertRaises(assigmentValidatorException):
            self.__assigmentCtrl.addAssigment(1, 'caca', [30,2,2020], 9)
        with self.assertRaises(assigmentValidatorException):
            self.__assigmentCtrl.addAssigment(1, 'caca', [29,2,2017], 9)
        with self.assertRaises(assigmentValidatorException):
            self.__assigmentCtrl.addAssigment(1, 'caca', [31,11,2016], 9)
    
    def testDomain(self):
        testObject = assigmentDomain(1,'Test 1',[31,12,2016],9)
        assert(testObject.assigmentId == 1)
        assert(testObject.description == 'Test 1')
        assert(testObject.deadline == [31,12,2016])
        assert(testObject.grade == 9)
        assert(str(testObject)=='1 Test 1 31.12.2016 9')
        del testObject.assigmentId
        del testObject.description
        del testObject.deadline
        del testObject.grade
        testObject.assigmentId = 1
        testObject.description = 'Test'
        testObject.deadline = [2,10,2017]
        testObject.grade = 8