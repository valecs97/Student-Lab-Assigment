'''
Created on Nov 26, 2016

@author: valec
'''
import unittest
from repository.gradeRepository import gradeRepository
from repository.assigmentRepository import assigmentRepository
from repository.studentRepository import studentRepository
from controller.undoRedoController import undoRedoController
from domain.studentDomain import studentDomain
from validator.valid import undoRedoValidatorException
from domain.assigmentDomain import assigmentDomain
from domain.gradeDomain import gradeDomain
from domain.commandDomain import commandDomain

class testUndoRedo(unittest.TestCase):
    
    def setUp(self):
        self.__studentRepo = studentRepository()
        self.__assigmentRepo = assigmentRepository()
        self.__gradeRepo = gradeRepository()
        self.__undoRedoCtrl = undoRedoController(self.__studentRepo,self.__assigmentRepo,self.__gradeRepo)
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        del self.__studentRepo
        del self.__assigmentRepo
        del self.__gradeRepo
        del self.__undoRedoCtrl
        unittest.TestCase.tearDown(self)
        
    def testSimpleAdd(self):
        student = studentDomain(1,'Testovici',916)
        self.__studentRepo.addStudent(student)
        self.__undoRedoCtrl.saveUndoInstruction('addS',[student])
        assigment = assigmentDomain(1,'Description test',[10,10,2017],9)
        self.__assigmentRepo.addAssigment(assigment)
        self.__undoRedoCtrl.saveUndoInstruction('addA', [assigment])
        self.assertEqual(self.__studentRepo.getAll(), [student])
        self.assertEqual(self.__assigmentRepo.getAll(), [assigment])
        self.__undoRedoCtrl.doTheUndo()
        self.assertEqual(self.__studentRepo.getAll(), [student])
        self.assertEqual(self.__assigmentRepo.getAll(), [])
        self.__undoRedoCtrl.doTheRedo()
        self.assertEqual(self.__studentRepo.getAll(), [student])
        self.assertEqual(self.__assigmentRepo.getAll(), [assigment])
        self.__undoRedoCtrl.doTheUndo()
        self.__undoRedoCtrl.doTheUndo()
        self.assertEqual(self.__studentRepo.getAll(), [])
        self.assertEqual(self.__assigmentRepo.getAll(), [])
        self.__undoRedoCtrl.doTheRedo()
        self.assertEqual(self.__studentRepo.getAll(), [student])
        self.assertEqual(self.__assigmentRepo.getAll(), [])
        self.__undoRedoCtrl.doTheRedo()
        self.assertEqual(self.__studentRepo.getAll(), [student])
        self.assertEqual(self.__assigmentRepo.getAll(), [assigment])
        grade = gradeDomain(1,1,8)
        self.__gradeRepo.addGrade(grade)
        self.assertEqual(self.__assigmentRepo.getAll(), [assigment])
        self.assertEqual(self.__gradeRepo.getAll(), [grade])
        self.__undoRedoCtrl.doTheUndo()
        self.assertEqual(self.__assigmentRepo.getAll(), [])
        self.assertEqual(self.__gradeRepo.getAll(), [])
        self.__gradeRepo.addGrade(grade)
        self.assertEqual(self.__studentRepo.getAll(), [student])
        self.assertEqual(self.__gradeRepo.getAll(), [grade])
        self.__undoRedoCtrl.doTheUndo()
        self.assertEqual(self.__studentRepo.getAll(), [])
        self.assertEqual(self.__gradeRepo.getAll(), [])
        student = studentDomain(1,'Testovici',917)
        self.__studentRepo.addStudent(student)
        self.__undoRedoCtrl.saveUndoInstruction('addS',[student])
        with self.assertRaises(undoRedoValidatorException):
            self.__undoRedoCtrl.doTheRedo()
        self.__undoRedoCtrl.doTheUndo()
        with self.assertRaises(undoRedoValidatorException):
            self.__undoRedoCtrl.doTheUndo()
            
    def testSimpleRemove(self):
        student = studentDomain(1,'Testovici',916)
        self.__studentRepo.addStudent(student)
        self.__undoRedoCtrl.saveUndoInstruction('addS',[student])
        assigment = assigmentDomain(1,'Description test',[10,15,2017],9)
        self.__assigmentRepo.addAssigment(assigment)
        self.__undoRedoCtrl.saveUndoInstruction('addA', [assigment])
        grade = gradeDomain(1,1,0)
        self.__gradeRepo.addGrade(grade)
        self.__undoRedoCtrl.saveUndoInstruction('addG', grade)
        grade = gradeDomain(1,1,8)
        self.__gradeRepo.updateGrade(grade)
        self.__undoRedoCtrl.saveUndoInstruction('addG', grade)
        self.__studentRepo.removeStudentById(1)
        self.__gradeRepo.removeGradeById((1,1))
        self.__undoRedoCtrl.saveUndoInstruction('delS', [student,grade])
        self.assertEqual(self.__studentRepo.getAll(), [])
        self.assertEqual(self.__gradeRepo.getAll(), [])
        self.__undoRedoCtrl.doTheUndo()
        self.assertEqual(self.__studentRepo.getAll(), [student])
        self.assertEqual(self.__gradeRepo.getAll(), [grade])
        self.__assigmentRepo.removeAssigmentById(1)
        self.__gradeRepo.removeGradeById((1,1))
        self.__undoRedoCtrl.saveUndoInstruction('delA', [assigment,grade])
        self.assertEqual(self.__assigmentRepo.getAll(), [])
        self.assertEqual(self.__gradeRepo.getAll(), [])
        self.__undoRedoCtrl.doTheUndo()
        self.assertEqual(self.__assigmentRepo.getAll(), [assigment])
        self.assertEqual(self.__gradeRepo.getAll(), [grade])
        command = commandDomain(1,1)
        command.instruction=2
        command.remember=2
        del command.instruction
        del command.remember
        
    def testSimpleUpdate(self):
        student = studentDomain(1,'Testovici',916)
        self.__studentRepo.addStudent(student)
        assigment = assigmentDomain(1,'Description test',[10,15,2017],9)
        self.__assigmentRepo.addAssigment(assigment)
        student.group=915
        assigment.grade = 10
        self.__studentRepo.updateStudent(student)
        student.group=916
        self.__undoRedoCtrl.saveUndoInstruction('updS', [student,student])
        self.__assigmentRepo.updateAssigment(assigment)
        assigment.grade=9
        self.__undoRedoCtrl.saveUndoInstruction('updA', [assigment,assigment])
        self.assertEqual(self.__studentRepo.getAll(), [student])
        self.assertEqual(self.__assigmentRepo.getAll(), [assigment])
        self.__undoRedoCtrl.doTheUndo()
        self.__undoRedoCtrl.doTheUndo()
        self.assertEqual(self.__studentRepo.getAll(), [student])
        self.assertEqual(self.__assigmentRepo.getAll(), [assigment])
        
    def testSimpleAssign(self):
        student0 = studentDomain(1,'Testovici0',916)
        student1 = studentDomain(2,'Testovici1',916)
        student2 = studentDomain(3,'Testovici2',916)
        assigment = assigmentDomain(1,'Description test',[10,15,2017],9)
        self.__studentRepo.addStudent(student0)
        self.__studentRepo.addStudent(student1)
        self.__studentRepo.addStudent(student2)
        self.__assigmentRepo.addAssigment(assigment)
        self.__undoRedoCtrl.saveUndoInstruction('addS', student0)
        self.__undoRedoCtrl.saveUndoInstruction('addS', student1)
        self.__undoRedoCtrl.saveUndoInstruction('addS', student2)
        self.__undoRedoCtrl.saveUndoInstruction('addA', assigment)
        grade = gradeDomain(1,1,5)
        self.__gradeRepo.addGrade(grade)
        self.__undoRedoCtrl.saveUndoInstruction('addAFS', grade)
        self.assertEqual(self.__gradeRepo.getAll(), [grade])
        self.__undoRedoCtrl.doTheUndo()
        self.assertEqual(self.__gradeRepo.getAll(), [])
        self.__undoRedoCtrl.doTheRedo()
        self.assertEqual(self.__gradeRepo.getAll(), [grade])
        self.__undoRedoCtrl.doTheUndo()
        grade0 = gradeDomain(1,1,5)
        grade1 = gradeDomain(1,2,6)
        grade2 = gradeDomain(1,3,7)
        self.__gradeRepo.addGrade(grade0)
        self.__gradeRepo.addGrade(grade1)
        self.__gradeRepo.addGrade(grade2)
        self.__undoRedoCtrl.saveUndoInstruction('addASG', [1,916])
        self.__undoRedoCtrl.doTheUndo()
        self.assertEqual(self.__gradeRepo.getAll(), [])
        self.__undoRedoCtrl.doTheRedo()
        