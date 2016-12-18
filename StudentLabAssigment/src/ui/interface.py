'''
Created on Nov 2, 2016

@author: Vitoc
'''
from validator.valid import gradeValidatorException, studentValidatorException,\
    assigmentValidatorException, gradeRepositoryException,\
    studentRepositoryException, assigmentRepositoryException,\
    undoRedoValidatorException
from domain.gradeDomain import gradeDomain
import random

class interface:

    def __init__(self, assigmentCtrl,gradeCtrl,studentCtrl,undoRedoCtrl):
        self.__assigmentCtrl = assigmentCtrl
        self.__gradeCtrl = gradeCtrl
        self.__studentCtrl = studentCtrl
        self.__undoRedoCtrl = undoRedoCtrl
        self.__commandList = {"1":self.__manageAssigmentsUi,"2":self.__manageStudentsUi,"3":self.__assignAssigmentUi,"4":self.__assignAssigmentGroupUi,'5':self.__gradeStudentUi,'6':self.__statisticsUi,'7':self.generateRandomStudents,'8':self.__doTheUndoUi,'9':self.__doTheRedoUi,'0':'nothing','easter egg':self.printListsUi}
        self.__assigmentCommandList = {'1':self.__addAssigmentUi,'2':self.__updateAssigmentUi,'3':self.__deleteAssigmentByIdUi,'4':self.__printAllAssigmentsUi,'5':self.__findAssigmentByIdUi,'0':'nothing'}
        self.__studentCommandList = {'1':self.__addStudentUi,'2':self.__updateStudentUi,'3':self.__deleteStudentByIdUi,'4':self.__printAllStudentUi,'5':self.__findStudentByIdUi,'0':'nothing'}
        self.__orderStudentsList = {'1':self.__orderStudentsUi1,'2':self.__orderStudentsUi2,'0':'nothing'}
        self.__statisticsList = {'1':self.__orderStudentsUi,'2':self.__lateStudentsUi,'3':self.__schoolSituationUi,'4':self.__assigmentGradesUi,'0':'nothing'}
        
    def __showPrincipalOptions(self):
        print('Please choose one of the commands above :')
        print('1.Manage assigments')
        print('2.Manage students')
        print('3.Assign an assigment to a student')
        print('4.Assign an assigment to a group of students')
        print('5.Grade a student')
        print('6.Statistics')
        print('7.Generate random students')
        print('8.Undo')
        print('9.Redo')
        print('0.Exit')
        
    def __readOption(self):
        toReturn = input('\nInput command :')
        return toReturn
    
    def __showAssigmentMenu(self):
        print('\nPlease choose one of the commands above :')
        print('1.Add an assigment')
        print('2.Update an assigment')
        print('3.Delete an assigment')
        print('4.Print all assigments')
        print('5.Find an assigment by id')
        print('0.Back')
    
    def __manageAssigmentsUi(self):
        self.__showAssigmentMenu()
        cmd = self.__readOption()
        if cmd == '0':
                return
        if cmd in self.__assigmentCommandList:
            self.__assigmentCommandList[cmd]()
        else:
            print('Invalid command!')
            
    def __readGrade(self):
        return int(input('\nGrade :'))
    
    def __readAssigmentId(self):
        return int(input('\nAssigment Id :'))
    
    def __readAssigmentDescription(self):
        return input('\nAssigment description :')
    
    def __readAssigmentDeadline(self):
        toReturn = input('\nAssigment deadline :').split('.')
        if len(toReturn)==3:
            return [int(toReturn[0]),int(toReturn[1]),int(toReturn[2])]
        else:
            return ['wrong','wrong','wrong']
    
    def __readAssigmentGrade(self):
        return int(input('\nAssigment grade :'))
    
    def __readStudentId(self):
        return int(input('\nStudent Id :'))
    
    def __readStudentName(self):
        return input('\nStudent name :')
    
    def __readStudentGroup(self):
        return int(input('\nStudent group :'))
        
    def __addAssigmentUi(self):
        assigmentId = self.__readAssigmentId()
        assigmentDescription = self.__readAssigmentDescription()
        assigmentDeadline = self.__readAssigmentDeadline()
        assigmentGrade = self.__readAssigmentGrade()
        self.__assigmentCtrl.addAssigment(assigmentId,assigmentDescription,assigmentDeadline,assigmentGrade)
        assigment = self.__assigmentCtrl.getById(assigmentId)
        self.__undoRedoCtrl.saveUndoInstruction('addA',[assigment])
    
    def __updateAssigmentUi(self):
        assigmentId = self.__readAssigmentId()
        assigmentDescription = self.__readAssigmentDescription()
        assigmentDeadline = self.__readAssigmentDeadline()
        assigmentGrade = self.__readAssigmentGrade()
        assigment = self.__assigmentCtrl.getById(assigmentId)
        self.__assigmentCtrl.updateAssigment(assigmentId,assigmentDescription,assigmentDeadline,assigmentGrade)
        assigment0 = self.__assigmentCtrl.getById(assigmentId)
        self.__undoRedoCtrl.saveUndoInstruction('updA',[assigment,assigment0])
    
    '''
    def __deleteAssigmentUi(self):
        assigmentId = self.__readAssigmentId()
        assigmentDescription = self.__readAssigmentDescription()
        assigmentDeadline = self.__readAssigmentDeadline()
        assigmentGrade = self.__readAssigmentGrade()
        self.__assigmentCtrl.deleteAssigment(assigmentId,assigmentDescription,assigmentDeadline,assigmentGrade)
    '''
    
    def __deleteAssigmentByIdUi(self):
        assigmentId = self.__readAssigmentId()
        assigment = self.__assigmentCtrl.getById(assigmentId)
        self.__assigmentCtrl.deleteAssigmentById(assigmentId)
        grades = self.__gradeCtrl.deleteAssigmentStudents(assigmentId)
        self.__saveDeleteAssigmentByIdUi(assigment, grades)
    
    def __saveDeleteAssigmentByIdUi(self,assigment,grades):
        remember=[]
        remember.append(assigment)
        for x in grades:
            remember.append(x)
        self.__undoRedoCtrl.saveUndoInstruction('delA',remember)
    
    def __printAllAssigmentsUi(self):
        st = ""
        for x in self.__assigmentCtrl.getAll():
            st += str(x) + "\n"
        print(st)
    
    def __findAssigmentByIdUi(self):
        assigmentId = self.__readAssigmentId()
        print(self.__assigmentCtrl.getById(assigmentId))
        
    def __showStudentMenu(self):
        print('\nPlease choose one of the commands above :')
        print('1.Add a student')
        print('2.Update a student')
        print('3.Delete a student')
        print('4.Print all students')
        print('5.Find a student by id')
        print('0.Back')
    
    def __manageStudentsUi(self):
        self.__showStudentMenu()
        cmd = self.__readOption()
        if cmd == '0':
                return
        if cmd in self.__studentCommandList:
            self.__studentCommandList[cmd]()
        else:
            print('Invalid command!')
    
    def __addStudentUi(self):
        studentId = self.__readStudentId()
        studentName = self.__readStudentName()
        studentGroup = self.__readStudentGroup()
        self.__studentCtrl.addStudent(studentId,studentName,studentGroup)
        student = self.__studentCtrl.getById(studentId)
        self.__undoRedoCtrl.saveUndoInstruction('addS',[student])
    
    def __updateStudentUi(self):
        studentId = self.__readStudentId()
        studentName = self.__readStudentName()
        studentGroup = self.__readStudentGroup()
        student = self.__studentCtrl.getById(studentId)
        self.__studentCtrl.updateStudent(studentId,studentName,studentGroup)
        student0 = self.__studentCtrl.getById(studentId)
        self.__undoRedoCtrl.saveUndoInstruction('updS',[student,student0])
        
    def __deleteStudentByIdUi(self):
        studentId = self.__readStudentId()
        student = self.__studentCtrl.getById(studentId)
        self.__studentCtrl.deleteStudentById(studentId)
        grades=self.__gradeCtrl.deleteStudentAssigments(studentId)
        self.__saveDeleteStudentByIdUi(student, grades)
        
    
    def __saveDeleteStudentByIdUi(self,student,grades):
        remember=[]
        remember.append(student)
        for x in grades:
            remember.append(x)
        self.__undoRedoCtrl.saveUndoInstruction('delS',remember)
    
    def __printAllStudentUi(self):
        st = ""
        for x in self.__studentCtrl.getAll():
            st += str(x) + "\n"
        print(st)
    
    def __findStudentByIdUi(self):
        studentId = self.__readStudentId()
        print(self.__studentCtrl.getById(studentId))
    
    def __assignAssigmentUi(self):
        assigmentId = self.__readAssigmentId()
        studentId = self.__readStudentId()
        self.__gradeCtrl.assignAssgiment(assigmentId,studentId)
        grade = gradeDomain(assigmentId,studentId,0)
        self.__undoRedoCtrl.saveUndoInstruction('addAFS',grade)
    
    def __assignAssigmentGroupUi(self):
        assigmentId = self.__readAssigmentId()
        group = self.__readStudentGroup()
        self.__gradeCtrl.assignAssigmentGroup(assigmentId,group)
        self.__undoRedoCtrl.saveUndoInstruction('addASG',[assigmentId,group])
            
    def __gradeStudentUi(self):
        studentId = self.__readStudentId()
        toPrint = self.__gradeCtrl.getAssigments(studentId)
        if toPrint==[]:
            print('There are no assigments to this student')
            return
        for i in range(len(toPrint)):
            aux=str(i+1)
            print(aux + '.' + 'Assigment number ' + str(toPrint[i][0]))
        command = self.__readOption()
        command = int(command)-1
        if command<0 or command>len(toPrint)-1:
            print('Invalid command')
            return
        grade = self.__readGrade()
        self.__gradeCtrl.updateGrade(int(toPrint[command][0]),int(toPrint[command][1]),grade)
        gradeD = gradeDomain(int(toPrint[command][0]),int(toPrint[command][1]),0)
        gradeD0 = gradeDomain(int(toPrint[command][0]),int(toPrint[command][1]),grade)
        self.__undoRedoCtrl.saveUndoInstruction('updG',[gradeD,gradeD0])
    
    def __printStatisticsOptions(self):
        print('1.Order students who got an assigment')
        print('2.Students who are late in a assigment')
        print('3.Students with best school situation')
        print('4.Grades from an assigment')
        print('0.Back')
    
    def __statisticsUi(self):
        self.__printStatisticsOptions()
        cmd = self.__readOption()
        if cmd == '0':
            return
        if cmd in self.__statisticsList:
            self.__statisticsList[cmd]()
        else:
            print('Invalid command!')
        
    def __assigmentGradesUi(self):
        assigmentId = self.__readAssigmentId()
        students = self.__gradeCtrl.assigmentGrades(assigmentId)
        for x in students:
            print (self.__studentCtrl.getById(x[0]),x[1])
        
    
    def __schoolSituationUi(self):
        studentAndGrade = self.__gradeCtrl.schoolSituation()
        if studentAndGrade==[]:
            print('There is no school situation')
            return
        for x in studentAndGrade:
            print(self.__studentCtrl.getById(x[0]), ' with grade ',x[1])
            
    
    def __lateStudentsUi(self):
        toPrint = self.__gradeCtrl.lateStudents()
        for x in toPrint:
            print(self.__studentCtrl.getById(x))
    
    def __orderStudentsOption(self):
        print('1.Alphabeticaly by an assigment')
        print('2.Avarage note by an assigment')
        print('0.Back')
        
    def __orderStudentsUi(self):
        self.__orderStudentsOption()
        cmd = self.__readOption()
        if cmd == '0':
                return
        if cmd in self.__orderStudentsList:
            self.__orderStudentsList[cmd]()
        else:
            print('Invalid command!')
            
    def __orderStudentsUi1(self):
        assigmentId = self.__readAssigmentId()
        studentIdList = self.__gradeCtrl.getStudents(assigmentId)
        students = []
        for x in studentIdList:
            students.append(self.__studentCtrl.getById(int(x[0])))
        students = sorted(students,key = lambda student: student.name)
        for x in students:
            print(x)
        
    
    def __orderStudentsUi2(self):
        assigmentId = self.__readAssigmentId()
        studentIdList = self.__gradeCtrl.getStudentsWithGrade(assigmentId)
        studentIdList = sorted(studentIdList, key = lambda student: student[1],reverse = True)
        students = []
        for x in studentIdList:
            students.append(self.__studentCtrl.getById(int(x[0])))
        for i in range(len(students)):
            print(students[i] , ' with grade ' , studentIdList[i][1])
            
    def __doTheUndoUi(self):
        self.__undoRedoCtrl.doTheUndo()
        
    def __doTheRedoUi(self):
        self.__undoRedoCtrl.doTheRedo()
    
    def generateRandomStudents(self):
        thing= self.__studentCtrl.getLen()
        for i in range(thing+1,thing+101):
            studentId=i
            studentNameLenght = random.randint(5,20)
            letter=random.randint(65,90)
            letter = str(chr(letter))
            studentName = letter
            for _ in range(studentNameLenght):
                letter=random.randint(97,122)
                letter = str(chr(letter))
                studentName+=letter
            studentGroup = random.randint(1,999)
            self.__studentCtrl.addStudent(studentId,studentName,studentGroup)
            
    def generateRandomAssigments(self):
        thing= self.__assigmentCtrl.getLen()
        for i in range(thing+1,thing+101):
            assigmentId=i
            assigmentLenghtDescription = random.randint(5,20)
            letter=random.randint(65,90)
            letter = str(chr(letter))
            assigmentDescription = letter
            for _ in range(assigmentLenghtDescription):
                letter=random.randint(97,122)
                letter = str(chr(letter))
                assigmentDescription+=letter
            day = random.randint(1,28)
            month = random.randint(1,12)
            year = random.randint(2017,2020)
            assigmentDate = [day,month,year]
            assigmentGrade=10
            self.__assigmentCtrl.addAssigment(assigmentId,assigmentDescription,assigmentDate,assigmentGrade)
            
    def generateRandomGrade(self):
        thing = self.__assigmentCtrl.getLen()
        for _ in range(thing+1,thing+101):
            studentId = random.randint(1,10)
            assigmentId = random.randint(1,10)
            try:
                self.__gradeCtrl.getById(assigmentId,studentId)
            except gradeRepositoryException:
                ok = random.randint(0,1)
                self.__gradeCtrl.assignAssgiment(assigmentId,studentId)
                if ok==1:
                    grade = random.randint(1,10)
                    self.__gradeCtrl.updateGrade(assigmentId,studentId,grade)
            
        
    def printListsUi(self):
        lists = self.__undoRedoCtrl.printLists()
        for x in lists[0]:
            try:
                print(str(x.remember[0]))
            except TypeError:
                print(str(x.remember))
        print('\n')
        for x in lists[1]:
            try:
                print(str(x.remember[0]))
            except TypeError:
                print(str(x.remember))
        
    '''
    This two functions adds 10 students and 10 assigments so that the lab teacher can test the program
    '''
    
    def __addTestAssigments(self):
        #self.__assigmentCtrl.addAssigment(1,'Desciption 1',[1,1,2017],10)
        self.__assigmentCtrl.addAssigment(2,'Desciption 2',[2,1,2017],9)
        self.__assigmentCtrl.addAssigment(3,'Desciption 3',[3,1,2017],8)
        self.__assigmentCtrl.addAssigment(4,'Desciption 4',[4,1,2017],7)
        self.__assigmentCtrl.addAssigment(5,'Desciption 5',[5,1,2017],6)
        self.__assigmentCtrl.addAssigment(6,'Desciption 6',[6,1,2017],5)
        self.__assigmentCtrl.addAssigment(7,'Desciption 7',[7,1,2017],4)
        self.__assigmentCtrl.addAssigment(8,'Desciption 8',[8,1,2017],3)
        self.__assigmentCtrl.addAssigment(9,'Desciption 9',[9,1,2017],2)
        self.__assigmentCtrl.addAssigment(10,'Desciption 10',[10,1,2017],10)
        
    def __addTestStudents(self):
        self.__studentCtrl.addStudent(1,'Test testovici 1',911)
        self.__studentCtrl.addStudent(2,'Test testovici 2',912)
        self.__studentCtrl.addStudent(3,'Test testovici 3',913)
        self.__studentCtrl.addStudent(4,'Test testovici 4',914)
        self.__studentCtrl.addStudent(5,'Test testovici 5',915)
        self.__studentCtrl.addStudent(6,'Test testovici 6',916)
        self.__studentCtrl.addStudent(7,'Test testovici 7',916)
        self.__studentCtrl.addStudent(8,'Test testovici 8',916)
        self.__studentCtrl.addStudent(9,'Test testovici 9',917)
        self.__studentCtrl.addStudent(10,'Test testovici 10',917)
        
    def __addTestGrade(self):
        self.__gradeCtrl.assignAssgiment(1,1)
        self.__gradeCtrl.assignAssgiment(2,1)
        self.__gradeCtrl.assignAssgiment(3,1)
        self.__gradeCtrl.assignAssgiment(1,2)
        self.__gradeCtrl.assignAssgiment(2,2)
        self.__gradeCtrl.assignAssgiment(3,2)
        self.__gradeCtrl.assignAssgiment(1,3)
        self.__gradeCtrl.assignAssgiment(2,3)
        self.__gradeCtrl.assignAssgiment(3,3)
        self.__gradeCtrl.assignAssgiment(1,4)
        self.__gradeCtrl.updateGrade(1,1,9)
        self.__gradeCtrl.updateGrade(2,1,9)
        self.__gradeCtrl.updateGrade(1,2,10)
        self.__gradeCtrl.updateGrade(2,2,9)
        self.__gradeCtrl.updateGrade(1,3,8)
        self.__gradeCtrl.updateGrade(2,3,9)
        

    '''
    This is the run functions , here it starts everything
    '''
    def run(self):
        #self.generateRandomAssigments()
        #self.generateRandomStudents()
        #self.generateRandomGrade()
        while True:
            self.__showPrincipalOptions()
            cmd = self.__readOption()
            if cmd == '0':
                return
            if cmd in self.__commandList:
                try:
                    self.__commandList[cmd]()
                except gradeValidatorException as gve:
                    print('Grade validation error :\n',gve)
                except studentValidatorException as sve:
                    print('Student validation error :\n',sve)
                except assigmentValidatorException as ave:
                    print('Assigment validation error :\n',ave)
                except gradeRepositoryException as gre:
                    print('Grade repository error :\n',gre)
                except studentRepositoryException as sre:
                    print('Student repository error :\n',sre)
                except assigmentRepositoryException as are:
                    print('Assigment repository error :\n',are)
                except undoRedoValidatorException as urve:
                    print('Undo / Redo validation error :\n',urve)
                #except ValueError:
                #    print('You have written something wrong , please make sure that all date is in the correct format')
            else:
                print('Invalid command!')