'''
Created on Nov 2, 2016

@author: Vitoc
'''
from test.testStudent import testStudent
from test.testGrade import testGrade

if __name__ == '__main__':
    pass

from controller.assigmentController import assigmentController
from controller.gradeController import gradeController
from controller.studentController import studentController
from repository.assigmentRepository import assigmentRepository
from repository.gradeRepository import gradeRepository
from repository.studentRepository import studentRepository
from ui.interface import interface
from test.testAssigments import testAssigments

testRepoAssigment = assigmentRepository()
testCtrlAssigment = assigmentController(testRepoAssigment)
test1 = testAssigments(testCtrlAssigment)
test1.run()

testRepoStudent = studentRepository()
testCtrlStudent = studentController(testRepoStudent)
test2 = testStudent(testCtrlStudent)
test2.run()

testRepoGrade = gradeRepository()
testCtrlGrade = gradeController(testRepoGrade)
test3= testGrade(testCtrlGrade)
test3.run()


repoAssigment = assigmentRepository()
repoGrade = gradeRepository()
repoStudent = studentRepository()
ctrlAssigment = assigmentController(repoAssigment)
ctrlGrade = gradeController(repoGrade)
ctrlStudent = studentController(repoStudent)
con = interface(ctrlAssigment,ctrlGrade,ctrlStudent)
con.run()