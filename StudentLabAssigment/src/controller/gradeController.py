'''
Created on Nov 2, 2016

@author: Vitoc
'''

from domain.gradeDomain import gradeDomain
from validator.valid import gradeValidator, gradeValidatorException
from _datetime import datetime

class gradeController:


    def __init__(self,repo,repoStudent,repoAssigment):
        self.__repo = repo
        self.__validate = gradeValidator()
        self.__repoStudent = repoStudent
        self.__repoAssigment = repoAssigment
        
    '''
    Function that assign an assigment to a student
    
    input data:
    studentId - integer
    assigmentId - integer
    
    Raises gradeValidationException if :
    1.The assigment Id is a negative number (P.S the ui function has a exception if the object is not a number)
    1.The student Id is a negative number
    
    note :
    The program will not verify if the student has the assigment.
    it will just verify if it exist so that it doesnt overwrite it
    '''    
    
    def assignAssgiment(self,assigmentId,studentId):
        self.__validate.idsValidator(assigmentId,studentId)
        self.__repoAssigment.findById(assigmentId)
        self.__repoStudent.findById(studentId)
        grade = gradeDomain(assigmentId,studentId,0)
        self.__repo + grade
    
    '''
    Function that given (or updates) a assigment grade to a student:
    
    input data:
    assigmentId - integer
    studentId - integer
    grade - integer
    
    Raises gradeValidationException if :
    1.The assigment Id is a negative number (P.S the ui function has a exception if the object is not a number)
    1.The student Id is a negative number
    3.The grade isnt between 1 and 10
    
    '''
    
    def updateGrade(self,assigmentId,studentId,grade):
        grade = gradeDomain(assigmentId,studentId,grade)
        self.__validate.gradeValidator(grade)
        assigment = self.__repoAssigment.findById(assigmentId)
        if grade.grade > assigment.grade:
            raise gradeValidatorException('Grade should be lower than the assigments maximum grade')
        oldGrade=self.getById(assigmentId, studentId)
        if oldGrade.grade!=0:
            raise gradeValidatorException('The grade is already assigned ! You cannot change it !')
        self.__repo.updateGrade(grade)
        
    '''
    Function that assigns an assigment to a group of student
    
    input data:
    assigmentId - integer
    group - integer
    
    Raises gradeValidatorException if there are no students in the group
    '''

    def assignAssigmentGroup(self,assigmentId,group):
        self.__repoAssigment.findById(assigmentId)
        ok=False
        for x in self.__repoStudent.getAll():
            if x.group==group:
                self.assignAssgiment(assigmentId,x.studentId)
                ok=True
        if ok==False:
            raise gradeValidatorException('There are no students in this group')

    '''
    Function that gets assigmentId by giving it a studentId
    
    input data:
    studentId - integer
    
    output data:
    a list of touples (assigmentId,studentId)
    
    Raises studentRepositoryException if:
    1.The studentId doesnt exist
    
    note:
    The first function (without "With Grade") will get all assigments ,the students have.
    The second one will only get the assigments that he got a grade for
    '''

    def getAssigments(self,studentId):
        self.__repoStudent[studentId]
        toReturn=[]
        for x in self.getAll():
            if x.studentId==studentId and x.grade==0:
                toReturn.append((x.assigmentId,x.studentId))
        return toReturn
    
    def getAssigmentsWithGrade(self,studentId):
        self.__repoStudent[studentId]
        toReturn=[]
        for x in self.getAll():
            if x.studentId==studentId and x.grade!=0:
                toReturn.append((x.assigmentId,x.studentId))
        return toReturn
      
    '''
    Function that gets studentId by giving it a assigmentId
    
    input data:
    assigmentId - integer
    
    output data:
    a list of touples (studentId,grade)
    
    Raises assigmentRepositoryException if:
    1.The assigmentId doesnt exist
    
    note:
    The first function (without "With Grade") will get all students with or without a grade.
    The second one will only get the students with a grade at this assigment
    '''
            
    def getStudents(self,assigmentId):
        self.__repoAssigment[assigmentId]
        toReturn=[]
        for x in self.getAll():
            if x.assigmentId==assigmentId:
                toReturn.append((x.studentId,x.grade))
        if toReturn==[]:
            raise gradeValidatorException('There are no students to this assigment')
        return toReturn
    
    def getStudentsWithGrade(self,assigmentId):
        self.__repoAssigment[assigmentId]
        toReturn=[]
        for x in self.getAll():
            if x.assigmentId==assigmentId and x.grade!=0:
                toReturn.append((x.studentId,x.grade))
        if toReturn==[]:
            raise gradeValidatorException('There are no grades to this assigment')
        return toReturn
    
    '''
    Function that searches for all late student with their assigments
    
    output data:
    a list of studentIds
    
    Raises gradeValidatorException if there are no such students
    '''
        
    def lateStudents(self):
        grades = self.getAll()
        toReturn = []
        for x in grades:
            if x.grade==0:
                assigment = self.__repoAssigment.findById(x.assigmentId)
                now = datetime.now()
                assigmentTime = assigment.deadline
                assigmentTime = datetime(assigmentTime[2],assigmentTime[1],assigmentTime[0])
                if now >assigmentTime:
                    toReturn.append(x.studentId)
        if toReturn == []:
            raise gradeValidatorException('There are no such students !')
        return toReturn
    
    '''
    Function that deletes assigments that a student had
    
    input data:
    studentId - integer
    '''
   
    def deleteStudentAssigments(self,studentId):
        toReturn = []
        for x in self.getAll():
            if x.studentId == studentId:
                toReturn.append(x)
                self.deleteGradeById(x.assigmentId,x.studentId)
        return toReturn
                
    '''
    Function that deletes students from an assigment
    
    input data:
    assigmentId - integer
    ''' 
                
    def deleteAssigmentStudents(self,assigmentId):
        toReturn = []
        for x in self.getAll():
            if x.assigmentId == assigmentId:
                toReturn.append(x)
                self.deleteGradeById(x.assigmentId,x.studentId)
        return toReturn
    
    '''
    Function that gets the school situation for every student apart
    
    output data:
    a list of touples (studentId, grade*)
    
    *the grade is an aritmetic media of all assigments
    '''
   
    def schoolSituation(self):
        students = self.__repoStudent.getAll()
        studentAndGrade=[]
        for student in students:
            assigments= self.getAssigmentsWithGrade(student.studentId)
            if assigments!=[]:
                grade=0
                for y in assigments:
                    gradeD=self.getById(y[0],y[1])
                    grade+=gradeD.grade
                grade = float(grade) / (len(assigments))
                studentAndGrade.append((student.studentId,grade))
        studentAndGrade = sorted(studentAndGrade,key = lambda stud : stud[1],reverse=True)
        return studentAndGrade
    
    '''
    Function that gets all the grades from an assigment order by the highest grade
    
    input data:
    assigmentId - integer
    
    output data:
    a list of touples (studentId, grade)
    '''
   
    def assigmentGrades(self,assigmentId):
        students = self.getStudentsWithGrade(assigmentId)
        students = sorted(students, key = lambda student : student[1],reverse = True)
        return students
        
    '''
    Function that deletes a grade (or assigment to a student)
    
    input data:
    studentId - integer
    assigmentId - integer
    ''' 
        
    def deleteGradeById(self,assigmentId,studentId):
        (assigmentId,studentId) - self.__repo
        
    '''
    def deleteAssigment(self,studentId,assigmentId,grade):
        grade = gradeDomain(assigmentId,studentId,grade)
        self.__validate.gradeValidator(grade)
        self.__repo - grade
    '''
        
    '''
    Function that gets a grade (or assigment to a stundet) by the id:
    
    input data:
    studentId - integer
    assigmentId - integer
    
    output data:
    gradeDomain
    ''' 
        
    def getById(self,assigmentId,studentId):
        return self.__repo[(assigmentId,studentId)]
    
    '''
    Function that gets all grades (or assigment to a student) :
    

    output data:
    a list of assigments gradeDomain
    ''' 
    
    def getAll(self):
        return self.__repo.getAll()