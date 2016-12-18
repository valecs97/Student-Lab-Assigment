'''
Created on Nov 6, 2016

@author: Vitoc
'''
from validator.valid import gradeValidatorException, gradeRepositoryException,\
    assigmentRepositoryException
from domain.gradeDomain import gradeDomain
import unittest
from controller.gradeController import gradeController
from repository.gradeRepository import gradeRepository
from repository.studentRepository import studentRepository
from repository.assigmentRepository import assigmentRepository
from domain.assigmentDomain import assigmentDomain
from domain.studentDomain import studentDomain

class testGrade(unittest.TestCase):

    def setUp(self):
        self.__gradeRepo = gradeRepository()
        self.__studentRepo = studentRepository()
        self.__assigmentRepo = assigmentRepository()
        self.__gradeCtrl = gradeController(self.__gradeRepo,self.__studentRepo,self.__assigmentRepo)
        unittest.TestCase.setUp(self)
        

    def tearDown(self):
        del self.__gradeRepo
        del self.__assigmentRepo
        del self.__studentRepo
        del self.__gradeCtrl
        unittest.TestCase.tearDown(self)
        

    def testAddFunction(self):
        testObject = assigmentDomain(1,'Test 1',[31,12,2016],9)
        self.__assigmentRepo.addAssigment(testObject)
        testObject = studentDomain(1,'Testovici',917)
        self.__studentRepo.addStudent(testObject)
        self.__gradeCtrl.assignAssgiment(1,1)
        toVerify= self.__gradeCtrl.getById(1,1)
        assert(toVerify.assigmentId == 1)
        assert(toVerify.studentId == 1)
        assert(toVerify.grade == 0)
        try:
            self.__gradeCtrl.assignAssgiment(2,-1)
            #assert(False)
        except gradeValidatorException:
            assert True
        try:
            self.__gradeCtrl.updateGrade(1, 1, 10)
        except gradeValidatorException:
            assert True
        self.__gradeCtrl.updateGrade(1, 1, 9)
    
    def testRemoveFunction(self):
        testObject = assigmentDomain(1,'Test 1',[31,12,2016],9)
        self.__assigmentRepo.addAssigment(testObject)
        testObject = studentDomain(1,'Testovici',917)
        self.__studentRepo.addStudent(testObject)
        self.__gradeCtrl.assignAssgiment(1,1)
        self.__gradeCtrl.deleteGradeById(1,1)
        try:
            self.__gradeCtrl.deleteGradeById(1,1)
            #assert(False)
        except gradeRepositoryException:
            assert(True)
            
    def testGroupAssigment(self):
        testObject = assigmentDomain(1,'Test 1',[31,12,2016],9)
        self.__assigmentRepo.addAssigment(testObject)
        testObject = studentDomain(1,'Testovici',917)
        self.__studentRepo.addStudent(testObject)
        self.__gradeCtrl.assignAssigmentGroup(1, 917)
        try:
            self.__gradeCtrl.assignAssigmentGroup(1, 916)
        except gradeValidatorException:
            assert True
        try:
            self.__gradeCtrl.assignAssigmentGroup(2, 999)
        except assigmentRepositoryException:
            assert True
            
    def testStudentAndAssigmentGetters(self):
        testObject = assigmentDomain(1,'Test 1',[31,12,2016],9)
        self.__assigmentRepo.addAssigment(testObject)
        testObject = studentDomain(1,'Testovici',917)
        self.__studentRepo.addStudent(testObject)
        self.__gradeCtrl.assignAssgiment(1, 1)
        self.assertEqual(self.__gradeCtrl.getAssigments(1), [(1,1)])
        self.assertEqual(self.__gradeCtrl.getStudents(1), [(1,0)])
        self.__gradeCtrl.deleteStudentAssigments(1)
        try:
            self.__gradeCtrl.getStudents(1)
        except gradeValidatorException:
            assert True
        self.__gradeCtrl.assignAssgiment(1, 1)
        self.__gradeCtrl.updateGrade(1, 1, 9)
        self.assertEqual(self.__gradeCtrl.getAssigmentsWithGrade(1),[(1,1)])
        self.assertEqual(self.__gradeCtrl.getStudentsWithGrade(1), [(1,9)])
        self.__gradeCtrl.deleteAssigmentStudents(1)
        try:
            self.__gradeCtrl.getStudentsWithGrade(1)
        except gradeValidatorException:
            assert True
        
    def testLateStudents(self):
        testObject = assigmentDomain(1,'Test 1',[31,12,2015],9)
        self.__assigmentRepo.addAssigment(testObject)
        testObject = studentDomain(1,'Testovici',917)
        self.__studentRepo.addStudent(testObject)
        self.__gradeCtrl.assignAssgiment(1, 1)
        self.assertEqual(self.__gradeCtrl.lateStudents(), [1])
        self.__gradeRepo.removeGradeById((1,1))
        with self.assertRaises(gradeValidatorException):
            self.__gradeCtrl.lateStudents()
        
    def testSchoolSituation(self):
        testObject = assigmentDomain(1,'Test 1',[31,12,2015],9)
        self.__assigmentRepo.addAssigment(testObject)
        testObject = studentDomain(1,'Testovici',917)
        self.__studentRepo.addStudent(testObject)
        self.__gradeCtrl.assignAssgiment(1, 1)
        self.__gradeCtrl.updateGrade(1, 1, 9)
        self.assertEqual(self.__gradeCtrl.schoolSituation(), [(1,9)])
        
    def testAssigmentGrades(self):
        testObject = assigmentDomain(1,'Test 1',[31,12,2015],9)
        self.__assigmentRepo.addAssigment(testObject)
        testObject = studentDomain(1,'Testovici',917)
        self.__studentRepo.addStudent(testObject)
        self.__gradeCtrl.assignAssgiment(1, 1)
        self.__gradeCtrl.updateGrade(1, 1, 9)
        self.assertEqual(self.__gradeCtrl.assigmentGrades(1), [(1,9)])
                
    def testGradeValidator(self):
        with self.assertRaises(gradeValidatorException):
            self.__gradeCtrl.assignAssgiment(-1, -1)
        with self.assertRaises(gradeValidatorException):
            self.__gradeCtrl.updateGrade(-1, -1, -1)
            
    def testGradeRepository(self):
        with self.assertRaises(gradeRepositoryException):
            self.__gradeRepo.findById(1)
        testObject = gradeDomain(1,1,1)
        testObject + self.__gradeRepo
        str(self.__gradeCtrl)
                
    def testDomain(self):
        testObject = gradeDomain(1,100,10)
        assert(testObject.studentId == 100)
        assert(testObject.assigmentId == 1)
        assert(testObject.grade == 10)
        assert(str(testObject)=='1 100 10')
        del testObject.studentId
        del testObject.assigmentId
        del testObject.grade
        testObject.studentId=1
        testObject.assigmentId=1
        testObject.grade=9