'''
Created on Nov 2, 2016

@author: Vitoc
'''
from validator.valid import gradeValidatorException, studentValidatorException,\
    assigmentValidatorException, gradeRepositoryException,\
    studentRepositoryException, assigmentRepositoryException

class interface:
    '''
    classdocs
    '''


    def __init__(self, assigmentCtrl,gradeCtrl,studentCtrl):
        self.__assigmentCtrl = assigmentCtrl
        self.__gradeCtrl = gradeCtrl
        self.__studentCtrl = studentCtrl
        self.__commandList = {"1":self.__manageAssigmentsUi,"2":self.__manageStudentsUi,"3":self.__assignAssigmentUi,"4":self.__assignAssigmentGroupUi,'0':'nothing'}
        self.__assigmentCommandList = {'1':self.__addAssigmentUi,'2':self.__updateAssigmentUi,'3':self.__deleteAssigmentByIdUi,'4':self.__printAllAssigmentsUi,'5':self.__findAssigmentByIdUi,'0':'nothing'}
        self.__studentCommandList = {'1':self.__addStudentUi,'2':self.__updateStudentUi,'3':self.__deleteStudentByIdUi,'4':self.__printAllStudentUi,'5':self.__findStudentByIdUi,'0':'nothing'}
        
    def __showPrincipalOptions(self):
        print('Please choose one of the commands above :')
        print('1.Manage assigments')
        print('2.Manage students')
        print('3.Assign an assigment to a student')
        print('4.Assign an assigment to a group of students')
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
    
    def __updateAssigmentUi(self):
        assigmentId = self.__readAssigmentId()
        assigmentDescription = self.__readAssigmentDescription()
        assigmentDeadline = self.__readAssigmentDeadline()
        assigmentGrade = self.__readAssigmentGrade()
        self.__assigmentCtrl.updateAssigment(assigmentId,assigmentDescription,assigmentDeadline,assigmentGrade)
    
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
        self.__assigmentCtrl.deleteAssigmentById(assigmentId)
        self.__deleteAssigmentStudentsUi(assigmentId)
    
    def __deleteAssigmentStudentsUi(self,assigmentId):
        l = ''
        for x in self.__gradeCtrl.getAll():
            l=str(x)
            l = l.split(' ')
            if l[0] == str(assigmentId):
                self.__gradeCtrl.deleteGradeById(int(l[0]),int(l[1]))
    
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
    
    def __updateStudentUi(self):
        studentId = self.__readStudentId()
        studentName = self.__readStudentName()
        studentGroup = self.__readStudentGroup()
        self.__studentCtrl.updateStudent(studentId,studentName,studentGroup)
        
    def __deleteStudentByIdUi(self):
        studentId = self.__readStudentId()
        self.__studentCtrl.deleteStudentById(studentId)
        self.__deleteStudentAssigmentsUi(studentId)
        
    def __deleteStudentAssigmentsUi(self,studentId):
        l = ''
        for x in self.__gradeCtrl.getAll():
            l=str(x)
            l = l.split(' ')
            if l[1] == str(studentId):
                self.__gradeCtrl.deleteGradeById(int(l[0]),int(l[1]))
        
    
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
        self.__assigmentCtrl.getById(assigmentId)
        studentId = self.__readStudentId()
        self.__studentCtrl.getById(studentId)
        self.__gradeCtrl.assignAssgiment(assigmentId,studentId)
    
    def __assignAssigmentGroupUi(self):
        assigmentId = self.__readAssigmentId()
        self.__assigmentCtrl.getById(assigmentId)
        group = self.__readStudentGroup()
        st = ""
        ok=False
        for x in self.__studentCtrl.getAll():
            st=str(x)
            st = st.split(' ')
            if st[len(st)-1]==str(group):
                self.__gradeCtrl.assignAssgiment(assigmentId,int(st[0]))
                ok=True
        if ok==False:
            print('There are no students in this group')
        
    '''
    This two functions adds 10 students and 10 assigments so that the lab teacher can test the program
    '''
    
    def __addTestAssigments(self):
        self.__assigmentCtrl.addAssigment(1,'Desciption 1',[1,1,2017],10)
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

    '''
    This is the run functions , here it starts everything
    '''
    def run(self):
        self.__addTestAssigments()
        self.__addTestStudents()
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
                except ValueError:
                    print('You have written something wrong , please make sure that all date is in the correct format')
            else:
                print('Invalid command!')