'''
Created on Nov 2, 2016

@author: Vitoc
'''

from controller.undoRedoController import undoRedoController
from ui.gui import gui
from repository.assigmentFileRepository import assigmentFileRepository
from repository.gradeFileRepository import gradeFileRepository
from repository.studentFileRepository import studentFileRepository
from domain.assigmentDomain import assigmentDomain
from domain.studentDomain import studentDomain
from domain.gradeDomain import gradeDomain
from settings import settings
from repository.assigmentRepository import assigmentRepository
from repository.gradeRepository import gradeRepository
from repository.studentRepository import studentRepository
from repository.assigmentPickleRepository import assigmentPickleRepository
from repository.gradePickleRepository import gradePickleRepository
from repository.studentPickleRepository import studentPickleRepository

if __name__ == '__main__':
    pass

from controller.assigmentController import assigmentController
from controller.gradeController import gradeController
from controller.studentController import studentController

from ui.interface import interface

import os
import sys

def checkGui():
    global cmd
    global guiSelected
    try:
        if settings['ui']=='gui':
            cmd = '2'
            guiSelected=True
        elif settings['ui']=='console':
            cmd = '1'
            guiSelected=True
    except:
        pass

def checkRandom():
    global con
    try:
        if settings['random']=='yes':
            con.generateRandomAssigments()
            con.generateRandomStudents()
            con.generateRandomGrade()
    except:
        pass
    
'''
Here it gets the path to the appdata folder
'''

dir_path = '%s\\StudentLabAssigment\\' %  os.environ['APPDATA'] 
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
sett = settings(dir_path+"settings.properties")
settings = sett.examineTheFile()
guiSelected = False

try:
    settings['assigments']
    settings['grades']
    settings['students']
except KeyError:
    print("The settings file has some bugs in it ... please delete if you dont find the problem")
    sys.exit()

'''
Here it check which type of repository the program should use
'''

if settings['repositoryType']=='inmemory':
    repoAssigment = assigmentRepository()
    repoGrade = gradeRepository()
    repoStudent = studentRepository()
    checkGui()
    
elif settings['repositoryType']=='textfiles':
    repoAssigment = assigmentFileRepository(dir_path + settings['assigments'],assigmentDomain.readAssigment,assigmentDomain.writeAssigment)
    repoGrade = gradeFileRepository(dir_path + settings['grades'],gradeDomain.readGrade,gradeDomain.writeGrade)
    repoStudent = studentFileRepository(dir_path + settings['students'],studentDomain.readStudent,studentDomain.writeStudent)
    checkGui()
    
elif settings['repositoryType']=='binaryfiles':
    repoAssigment = assigmentPickleRepository(dir_path + settings['assigments'])
    repoGrade = gradePickleRepository(dir_path + settings['grades'])
    repoStudent = studentPickleRepository(dir_path + settings['students'])
    checkGui()
else:
    print("The settings file has some bugs in it ... please delete if you dont find the problem")
    sys.exit()
    
'''
Here it creates the controllers
'''

ctrlAssigment = assigmentController(repoAssigment)
ctrlStudent = studentController(repoStudent)
ctrlGrade = gradeController(repoGrade,repoStudent,repoAssigment)
ctrlUndoRedo = undoRedoController(repoStudent,repoAssigment,repoGrade)

'''
Here it starts the gui
'''

if guiSelected == False:
    print('Please choose :')
    print('1.Console based Ui')
    print('2.Gui')
    cmd = input('input command:')
if cmd=='1':
    con = interface(ctrlAssigment,ctrlGrade,ctrlStudent,ctrlUndoRedo)
    checkRandom()
    con.run()
elif cmd=='2':
    con = gui(ctrlAssigment,ctrlGrade,ctrlStudent,ctrlUndoRedo)
    checkRandom()
    con.startUI()
else:
    print("Invalid command !")