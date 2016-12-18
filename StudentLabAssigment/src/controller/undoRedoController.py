'''
Created on Nov 26, 2016

@author: valec
'''
from domain.commandDomain import commandDomain
from validator.valid import undoRedoValidatorException
from domain.gradeDomain import gradeDomain

class undoRedoController:

    def __init__(self, studentRepo,assigmentRepo,gradeRepo):
        self.__studentRepo = studentRepo
        self.__assigmentRepo = assigmentRepo
        self.__gradeRepo = gradeRepo
        self.__undoList= []
        self.__redoList= []
        self.__undoCommands = {'addA':self.__removeAssigment,'updA':self.__updateAssigmentUndo,'delA':self.__addAssigment,'addS':self.__removeStudent,'updS':self.__updateStudentUndo,'delS':self.__addStudent,'addAFS':self.__removeAssigmentFromStudent,'addASG':self.__removeAssigmentFromGroup,'addG':self.__removeGrade,'updG':self.__updateGradeUndo}
        self.__redoCommands = {'addA':self.__addAssigment,'updA':self.__updateAssigmentRedo,'delA':self.__removeAssigment,'addS':self.__addStudent,'updS':self.__updateStudentRedo,'delS':self.__removeStudent,'addAFS':self.__addAssigmentToStudent,'addASG':self.__addAssigmentToGroup,'addG':self.__addGrade,'updG':self.__updateGradeRedo}
        
    '''
    Function that saves an undo instruction
    
    input data:
    instruction - string of chars
    remember - depends (list , assigmentDomain, studentDomain,gradeDomain)
    '''
    def saveUndoInstruction(self,instruction,remember):
        command = commandDomain(instruction,remember)
        self.__undoList.append(command)
        self.__deleteRedoInstruction()
      
    '''
    Function that saves an undo instruction
    
    input data:
    instruction - string of chars
    remember - depends (list , assigmentDomain, studentDomain,gradeDomain)
    
    note: this function does not remove the redo list
    '''  
        
    def __saveUndoInstructionWithoutRemoving(self,instruction,remember):
        command = commandDomain(instruction,remember)
        self.__undoList.append(command)
               
    '''
    Function that saves an redo operation directly from the undo list
    '''            
                
    def __saveRedoInstruction(self):
        command = self.__undoList[len(self.__undoList)-1]
        self.__redoList.append(command)
    
    '''
    Function that deletes the redo list
    '''
            
    def __deleteRedoInstruction(self):
        self.__redoList=[]
     
    '''
    Function that adds an assigment to the repository, also the grades from it
    
    input data:
    command - list , first element is a assigmentDomain , the rest (if they exist) are gradeDomain
    ''' 
        
    def __addAssigment(self,command):
        self.__assigmentRepo.addAssigment(command[0])
        for x in range(1,len(command)):
            self.__addGrade(command[x])
            
    '''
    Function that removes an assigment from the repository, also the grades from it
    
    input data:
    command - list , first element is a assigmentDomain , the rest (if they exist) are gradeDomain
    
    note : in this function the grades are useless , only the add function uses them
    We need to remember them as well in chase the user need to undo the modification
    '''
    
    def __removeAssigment(self,command):
        self.__assigmentRepo.removeAssigmentById(command[0].assigmentId)
        for x in self.__gradeRepo.getAll():
            if x.assigmentId == command[0].assigmentId:
                self.__removeGrade((x.assigmentId,x.studentId))
    '''
    Functions that updates an assigment from the repository
    
    input data:
    command - list of 2 assigmentDomains , the first one is the old one used by undo
    and the second one is the new one used by redo
    '''
                
    def __updateAssigmentUndo(self,command):
        self.__assigmentRepo.updateAssigment(command[0])
        
    def __updateAssigmentRedo(self,command):
        self.__assigmentRepo.updateAssigment(command[1])
    
    '''
    Function that adds a student to the repository, also the grades from him/her/apache_helicopter
    
    input data:
    command - list ,first element is a studentDomain , the rest are the grades
    '''
    
    def __addStudent(self,command):
        self.__studentRepo.addStudent(command[0])
        for x in range(1,len(command)):
            self.__addGrade(command[x])
    
    '''
    Function that removes a student from the repository, also the grades from him/her/apache_helicopter
    
    input data:
    command - list ,first element is a studentDomain , the rest are the grades
    
    note : in this function the grades are useless , only the add function uses them
    We need to remember them as well in chase the user need to undo the modification
    '''
    
    def __removeStudent(self,command):
        self.__studentRepo.removeStudentById(command[0].studentId)
        for x in self.__gradeRepo.getAll():
            if x.studentId == command[0].studentId:
                self.__removeGrade((x.assigmentId,x.studentId))
    
    '''
    Function that updates a student
    
    input data:
    command - a list of 2 studentDomain , the first one is the old one used by undo
    and the second one is the new one used by redo
    '''
    def __updateStudentUndo(self,command):
        self.__studentRepo.updateStudent(command[0])
        
    def __updateStudentRedo(self,command):
        self.__studentRepo.updateStudent(command[1])
    
    '''
    Function that removes an assigment from a student
    
    input data:
    command- gradeDomain
    '''
    
    def __removeAssigmentFromStudent(self,command):
        self.__gradeRepo.removeGradeById((command.assigmentId,command.studentId))
    
    '''
    Function that removes an assigment from a group of students
    
    input data:
    command - a list composed of 2 elements :
        assigmentId - integer
        group - integer
    '''
    
    def __removeAssigmentFromGroup(self,command):
        assigmentId = command[0]
        group = command[1]
        for x in self.__studentRepo.getAll():
            if x.group == group:
                self.__removeGrade((assigmentId,x.studentId))
    
    '''
    Function that removes a grade from a student
    
    input data:
    command - gradeDomain
    '''
    
    def __removeGrade(self,command):
        self.__gradeRepo.removeGradeById(command)
    
    '''
    Function that adds a grade to a student
    
    input data:
    command - gradeDomain
    '''
    
    def __addGrade(self,command):
        self.__gradeRepo.addGrade(command)
       
    '''
    Function that upgrades a grade to a student
    
    input data:
    command - a list of 2 gradeDomains , the first one is the old one used by undo
    and the second one is the new one used by redo
    '''
        
    def __updateGradeUndo(self,command):
        self.__gradeRepo.updateGrade(command[0])
    
    def __updateGradeRedo(self,command):
        self.__gradeRepo.updateGrade(command[1])
    
    '''
    Function that adds an assigment to a student
    
    input data:
    command - gradeDomain
    '''
    
    def __addAssigmentToStudent(self,command):
        self.__gradeRepo.addGrade(command)
    
    '''
    Function that adds an assigment to a group of students
    
    input data:
    command - gradeDomain
    '''
    
    def __addAssigmentToGroup(self,command):
        assigmentId = command[0]
        group = command[1]
        for x in self.__studentRepo.getAll():
            if x.group == group:
                self.__gradeRepo.addGrade(gradeDomain(assigmentId,x.studentId,0))
                
    '''
    Easter egg function
    '''
                
    def printLists(self):
        return [self.__undoList,self.__redoList]
    
    '''
    Function that reverse an operation done by the user
    
    raises :
    undoRedoValidatorException - if there are no more undos
    '''
    
    def doTheUndo(self):
        try:
            command = self.__undoList[len(self.__undoList)-1]
        except:
            raise undoRedoValidatorException('There are no more undos')
        self.__saveRedoInstruction()
        self.__undoCommands[command.instruction](command.remember)
        del self.__undoList[len(self.__undoList)-1]
        
    '''
    Function that redoes an operation done by the user
    
    raises :
    undoRedoValidatorException - if there are no more redos
    '''
        
    def doTheRedo(self):
        try:
            command = self.__redoList[len(self.__redoList)-1]

        except:
            raise undoRedoValidatorException('There are no more redos')
        self.__saveUndoInstructionWithoutRemoving(command.instruction, command.remember)
        self.__redoCommands[command.instruction](command.remember)
        del self.__redoList[len(self.__redoList)-1]