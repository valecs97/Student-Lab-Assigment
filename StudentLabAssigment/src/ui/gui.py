'''
Created on Dec 2, 2016

@author: Vitoc
'''
import random
from tkinter import *
from tkinter import messagebox
from validator.valid import assigmentValidatorException,\
    assigmentRepositoryException, gradeRepositoryException,\
    studentValidatorException, studentRepositoryException,\
    undoRedoValidatorException
from domain.gradeDomain import gradeDomain

class gui:
    """
      Implement the graphic user interface for add/list students
    """
    def __init__(self, assigmentCtrl,gradeCtrl,studentCtrl,undoRedoCtrl):
        self.__assigmentCtrl = assigmentCtrl
        self.__gradeCtrl = gradeCtrl
        self.__studentCtrl = studentCtrl
        self.__undoRedoCtrl = undoRedoCtrl

    def startUI(self):
        self.tk = Tk()
        self.tk.title("Student Lab Assigment")
        frame = Frame(self.tk)
        frame.pack()
        self.frame = frame
        '''
        lbl = Label(frame, text="ID:")
        lbl.pack(side=LEFT)

        self.idtf = Entry(frame, {})
        self.idtf.pack(side=LEFT)

        lbl = Label(frame, text="Name:")
        lbl.pack(side=LEFT)

        self.nametf = Entry(frame, {})
        self.nametf.pack(side=LEFT)

        lbl = Label(frame, text="Street:")
        lbl.pack(side=LEFT)

        self.streettf = Entry(frame, {})
        self.streettf.pack(side=LEFT)

        lbl = Label(frame, text="Nr.:")
        lbl.pack(side=LEFT)

        self.nrtf = Entry(frame, {})
        self.nrtf.pack(side=LEFT)

        lbl = Label(frame, text="City:")
        lbl.pack(side=LEFT)

        self.citytf = Entry(frame, {})
        self.citytf.pack(side=LEFT)
        '''
        try:
            self.manageAssigmentsBtn = Button(frame, text="Manage Assigments", command=self.__manageAssigmentsUi)
            self.manageAssigmentsBtn.pack(side=TOP)
            self.manageStudentsBtn = Button(frame, text="Manage Students", command=self.__manageStudentsUi)
            self.manageStudentsBtn.pack(side=TOP)
            self.assignAssigmentBtn = Button(frame, text="Assign Assigments", command = self.__assignAssigmentUi)
            self.assignAssigmentBtn.pack(side=TOP)
            self.gradeAStudentBtn = Button(frame, text="Grade a student", command = self.__gradeAStudentUi)
            self.gradeAStudentBtn.pack(side=TOP)
            self.statisticsBtn = Button(frame, text="Statistics", command = self.__statisticsUi)
            self.statisticsBtn.pack(side=TOP)
            self.undoBtn = Button(frame, text="Undo", command = self.__undoUi)
            self.undoBtn.pack(side=TOP)
            self.redoBtn = Button(frame, text="Redo", command = self.__redoUi)
            self.redoBtn.pack(side=TOP)
        except Exception as ex:
            messagebox.showerror('Error', ex)
        self.quitButton = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.quitButton.pack(side=TOP)
        self.tk.mainloop()
        
    def __manageAssigmentsUi(self):
        self.tk = Tk()
        self.tk.title("Manage Assigments")
        frameManageAssigments = Frame(self.tk)
        frameManageAssigments.pack()
        self.frame = frameManageAssigments
        self.addABtn = Button(frameManageAssigments,text='Add assigment', command = self.__addAssigmentUi)
        self.addABtn.pack(side=TOP)
        self.updateABtn = Button(frameManageAssigments,text='Update assigment', command = self.__updateAssigmentUi)
        self.updateABtn.pack(side=TOP)
        self.deleteABtn = Button(frameManageAssigments,text='Delete assigment', command = self.__deleteAssigmentUi)
        self.deleteABtn.pack(side=TOP)
        self.printABtn = Button(frameManageAssigments,text='Print all assigments', command = self.__printAssigments)
        self.printABtn.pack(side=TOP)
        self.findABtn = Button(frameManageAssigments,text='Find assigment', command = self.__findAssigmentByIdUi)
        self.findABtn.pack(side=TOP)
        #self.quitButton = Button(frameManageAssigments, text="QUIT", fg="red", command=frameManageAssigments.quit)
        #self.quitButton.pack(side=TOP)
        
    def __addAssigmentUi(self):
        self.tk = Tk()
        self.tk.title("Add assigment")
        frameAddA = Frame(self.tk)
        frameAddA.pack()
        self.frame = frameAddA
        lbl = Label(frameAddA, text="ID:")
        lbl.pack(side=LEFT)
        self.idA = Entry(frameAddA, {})
        self.idA.pack(side=LEFT)
        lbl = Label(frameAddA, text="Description:")
        lbl.pack(side=LEFT)
        self.descriptionA = Entry(frameAddA, {})
        self.descriptionA.pack(side=LEFT)
        lbl = Label(frameAddA, text="Deadline:")
        lbl.pack(side=LEFT)
        self.deadlineA = Entry(frameAddA, {})
        self.deadlineA.pack(side=LEFT)
        lbl = Label(frameAddA, text="Grade:")
        lbl.pack(side=LEFT)
        self.gradeA = Entry(frameAddA, {})
        self.gradeA.pack(side=LEFT)
        self.ctrlAddABtn = Button(frameAddA,text="Add",command = self.__addAssigment)
        self.ctrlAddABtn.pack(side=BOTTOM)
        
        #self.quitButton = Button(frameAddA, text="QUIT", fg="red", command=frameAddA.quit)
        #self.quitButton.pack(side=TOP)
    
    def __addAssigment(self):
        try:
            assigmentId = int(self.idA.get())
            assigmentDescription = self.descriptionA.get()
            assigmentDeadline = self.deadlineA.get().split('.')
            assigmentDeadline = [int(assigmentDeadline[0]),int(assigmentDeadline[1]),int(assigmentDeadline[2])]
            assigmentGrade = int(self.gradeA.get())
            self.__assigmentCtrl.addAssigment(assigmentId,assigmentDescription,assigmentDeadline,assigmentGrade)
            assigment = self.__assigmentCtrl.getById(assigmentId)
            self.__undoRedoCtrl.saveUndoInstruction('addA',[assigment])
            messagebox.showinfo('Please change this title', 'Done !')
        except assigmentValidatorException as ex:
            messagebox.showerror('Assigment Validator Exception', ex)
        except assigmentRepositoryException as ex:
            messagebox.showerror('Assigment Repository Exception', ex)
        except:
            messagebox.showerror('Error', 'Watch your input !')
        
            
    def __updateAssigmentUi(self):
        self.tk = Tk()
        self.tk.title("Update assigment")
        frameUpdA = Frame(self.tk)
        frameUpdA.pack()
        self.frame = frameUpdA
        lbl = Label(frameUpdA, text="ID:")
        lbl.pack(side=LEFT)
        self.idA = Entry(frameUpdA, {})
        self.idA.pack(side=LEFT)
        lbl = Label(frameUpdA, text="Description:")
        lbl.pack(side=LEFT)
        self.descriptionA = Entry(frameUpdA, {})
        self.descriptionA.pack(side=LEFT)
        lbl = Label(frameUpdA, text="Deadline:")
        lbl.pack(side=LEFT)
        self.deadlineA = Entry(frameUpdA, {})
        self.deadlineA.pack(side=LEFT)
        lbl = Label(frameUpdA, text="Grade:")
        lbl.pack(side=LEFT)
        self.gradeA = Entry(frameUpdA, {})
        self.gradeA.pack(side=LEFT)
        self.ctrlUpdateABtn = Button(frameUpdA,text="Update",command = self.__updateAssigment)
        self.ctrlUpdateABtn.pack(side=BOTTOM)
        #self.quitButton = Button(frameUpdA, text="QUIT", fg="red", command=frameUpdA.quit)
        #self.quitButton.pack(side=TOP)
    
    def __updateAssigment(self):
        try:
            assigmentId = int(self.idA.get())
            assigmentDescription = self.descriptionA.get()
            assigmentDeadline = self.deadlineA.get().split('.')
            assigmentDeadline = [int(assigmentDeadline[0]),int(assigmentDeadline[1]),int(assigmentDeadline[2])]
            assigmentGrade = int(self.gradeA.get())
            assigment = self.__assigmentCtrl.getById(assigmentId)
            self.__assigmentCtrl.updateAssigment(assigmentId,assigmentDescription,assigmentDeadline,assigmentGrade)
            assigment0 = self.__assigmentCtrl.getById(assigmentId)
            self.__undoRedoCtrl.saveUndoInstruction('updA',[assigment,assigment0])
            messagebox.showinfo('Please change this title', 'Done !')
        except assigmentValidatorException as ex:
            messagebox.showerror('Assigment Validator Exception', ex)
        except assigmentRepositoryException as ex:
            messagebox.showerror('Assigment Repository Exception', ex)
        except:
            messagebox.showerror('Error', 'Watch your input !')
        
    
    def __deleteAssigmentUi(self):
        self.tk = Tk()
        self.tk.title("Delete assigment")
        frameDelA = Frame(self.tk)
        frameDelA.pack()
        self.frame = frameDelA
        lbl = Label(frameDelA, text="ID:")
        lbl.pack(side=LEFT)
        self.idA = Entry(frameDelA, {})
        self.idA.pack(side=LEFT)
        self.ctrlDeleteABtn = Button(frameDelA,text="Delete",command = self.__deleteAssigment)
        self.ctrlDeleteABtn.pack(side=BOTTOM)
        #self.quitButton = Button(frameDelA, text="QUIT", fg="red", command=frameDelA.quit)
        #self.quitButton.pack(side=TOP)
    
    def __deleteAssigment(self):
        try:
            assigmentId = int(self.idA.get())
            assigment = self.__assigmentCtrl.getById(assigmentId)
            self.__assigmentCtrl.deleteAssigmentById(assigmentId)
            grades = self.__gradeCtrl.deleteAssigmentStudents(assigmentId)
            self.__saveDeleteAssigmentByIdUi(assigment, grades)
            messagebox.showinfo('Please change this title', 'Done !')
        except assigmentValidatorException as ex:
            messagebox.showerror('Assigment Validator Exception', ex)
        except assigmentRepositoryException as ex:
            messagebox.showerror('Assigment Repository Exception', ex)
        except:
            messagebox.showerror('Error', 'Watch your input !')
        
        
    def __saveDeleteAssigmentByIdUi(self,assigment,grades):
        remember=[]
        remember.append(assigment)
        for x in grades:
            remember.append(x)
        self.__undoRedoCtrl.saveUndoInstruction('delA',remember)
        
    def __printAssigmentsUi(self,st):
        self.tk = Tk()
        self.tk.title("Print assigments")
        framePrintA = Frame(self.tk)
        framePrintA.pack()
        self.frame = framePrintA
        lbl = Label(framePrintA, text=st)
        lbl.pack(side=TOP)
        #self.quitButton = Button(framePrintA, text="QUIT", fg="red", command=framePrintA.quit)
        #self.quitButton.pack(side=TOP)
    
    def __printAssigments(self):
        st = ""
        for x in self.__assigmentCtrl.getAll():
            st += str(x) + "\n"
        self.__printAssigmentsUi(st)
    
    def __findAssigmentByIdUi(self):
        self.tk = Tk()
        self.tk.title("Find assigment")
        frameFindA = Frame(self.tk)
        frameFindA.pack()
        self.frame = frameFindA
        lbl = Label(frameFindA, text="ID:")
        lbl.pack(side=TOP)
        self.idA = Entry(frameFindA, {})
        self.idA.pack(side=TOP)
        self.ctrlFindABtn = Button(frameFindA,text="Find it",command = self.__findAssigmentById)
        self.ctrlFindABtn.pack(side=BOTTOM)
        #self.quitButton = Button(frameFindA, text="QUIT", fg="red", command=frameFindA.quit)
        #self.quitButton.pack(side=TOP)
    
    def __findAssigmentById(self):
        try:
            assigment = self.__assigmentCtrl.getById(int(self.idA.get()))
            messagebox.showinfo('Look a title',assigment)
        except assigmentValidatorException as ex:
            messagebox.showerror('Assigment Validator Exception', ex)
        except assigmentRepositoryException as ex:
            messagebox.showerror('Assigment Repository Exception', ex)
        except:
            messagebox.showerror('Error', 'Watch your input !')
    
    def __manageStudentsUi(self):
        self.tk = Tk()
        self.tk.title("Manage Students")
        frameManageStudents = Frame(self.tk)
        frameManageStudents.pack()
        self.frame = frameManageStudents
        self.addSBtn = Button(frameManageStudents,text='Add student', command = self.__addStudentUi)
        self.addSBtn.pack(side=TOP)
        self.updateSBtn = Button(frameManageStudents,text='Update student', command = self.__updateStudentUi)
        self.updateSBtn.pack(side=TOP)
        self.deleteSBtn = Button(frameManageStudents,text='Delete student', command = self.__deleteStudentUi)
        self.deleteSBtn.pack(side=TOP)
        self.printSBtn = Button(frameManageStudents,text='Print all students', command = self.__printStudents)
        self.printSBtn.pack(side=TOP)
        self.findSBtn = Button(frameManageStudents,text='Find student', command = self.__findStudentByIdUi)
        self.findSBtn.pack(side=TOP)
        #self.quitButton = Button(frameManageStudents, text="QUIT", fg="red", command=frameManageStudents.quit)
        #self.quitButton.pack(side=TOP)
    
    def __addStudentUi(self):
        self.tk = Tk()
        self.tk.title("Add student")
        frameAddS = Frame(self.tk)
        frameAddS.pack()
        self.frame = frameAddS
        lbl = Label(frameAddS, text="ID:")
        lbl.pack(side=LEFT)
        self.idS = Entry(frameAddS, {})
        self.idS.pack(side=LEFT)
        lbl = Label(frameAddS, text="Name:")
        lbl.pack(side=LEFT)
        self.nameS = Entry(frameAddS, {})
        self.nameS.pack(side=LEFT)
        lbl = Label(frameAddS, text="Group:")
        lbl.pack(side=LEFT)
        self.groupS = Entry(frameAddS, {})
        self.groupS.pack(side=LEFT)
        self.ctrlAddSBtn = Button(frameAddS,text="Add",command = self.__addStudent)
        self.ctrlAddSBtn.pack(side=BOTTOM)
    
    def __addStudent(self):
        try:
            studentId = int(self.idS.get())
            studentName = self.nameS.get()
            studentGroup = int(self.groupS.get())
            self.__studentCtrl.addStudent(studentId,studentName,studentGroup)
            student = self.__studentCtrl.getById(studentId)
            self.__undoRedoCtrl.saveUndoInstruction('addS',[student])
            messagebox.showinfo('Please change this title', 'Done !')
        except studentValidatorException as ex:
            messagebox.showerror('Student Validator Exception', ex)
        except studentRepositoryException as ex:
            messagebox.showerror('Student Repository Exception', ex)
        except:
            messagebox.showerror('Error', 'Watch your input !')
    
    def __updateStudentUi(self):
        self.tk = Tk()
        self.tk.title("Update student")
        frameUpdateS = Frame(self.tk)
        frameUpdateS.pack()
        self.frame = frameUpdateS
        lbl = Label(frameUpdateS, text="ID:")
        lbl.pack(side=LEFT)
        self.idS = Entry(frameUpdateS, {})
        self.idS.pack(side=LEFT)
        lbl = Label(frameUpdateS, text="Name:")
        lbl.pack(side=LEFT)
        self.nameS = Entry(frameUpdateS, {})
        self.nameS.pack(side=LEFT)
        lbl = Label(frameUpdateS, text="Group:")
        lbl.pack(side=LEFT)
        self.groupS = Entry(frameUpdateS, {})
        self.groupS.pack(side=LEFT)
        self.ctrlUpdateSBtn = Button(frameUpdateS,text="Update",command = self.__updateStudent)
        self.ctrlUpdateSBtn.pack(side=BOTTOM)
    
    def __updateStudent(self):
        try:
            studentId = int(self.idS.get())
            studentName = self.nameS.get()
            studentGroup = int(self.groupS.get())
            student = self.__studentCtrl.getById(studentId)
            self.__studentCtrl.updateStudent(studentId,studentName,studentGroup)
            student0 = self.__studentCtrl.getById(studentId)
            self.__undoRedoCtrl.saveUndoInstruction('updS',[student,student0])
            messagebox.showinfo('Please change this title', 'Done !')
        except studentValidatorException as ex:
            messagebox.showerror('Student Validator Exception', ex)
        except studentRepositoryException as ex:
            messagebox.showerror('Student Repository Exception', ex)
        except:
            messagebox.showerror('Error', 'Watch your input !')
    
    def __deleteStudentUi(self):
        self.tk = Tk()
        self.tk.title("Delete student")
        frameDeleteS = Frame(self.tk)
        frameDeleteS.pack()
        self.frame = frameDeleteS
        lbl = Label(frameDeleteS, text="ID:")
        lbl.pack(side=LEFT)
        self.idS = Entry(frameDeleteS, {})
        self.idS.pack(side=LEFT)
        self.ctrlDeleteSBtn = Button(frameDeleteS,text="Delete",command = self.__deleteStudent)
        self.ctrlDeleteSBtn.pack(side=BOTTOM)
    
    def __deleteStudent(self):
        try:
            studentId = int(self.idS.get())
            student = self.__studentCtrl.getById(studentId)
            self.__studentCtrl.deleteStudentById(studentId)
            grades=self.__gradeCtrl.deleteStudentAssigments(studentId)
            self.__saveDeleteStudentByIdUi(student, grades)
            messagebox.showinfo('Please change this title', 'Done !')
        except studentValidatorException as ex:
            messagebox.showerror('Student Validator Exception', ex)
        except studentRepositoryException as ex:
            messagebox.showerror('Student Repository Exception', ex)
        except:
            messagebox.showerror('Error', 'Watch your input !')
            
    def __saveDeleteStudentByIdUi(self,student,grades):
        remember=[]
        remember.append(student)
        for x in grades:
            remember.append(x)
        self.__undoRedoCtrl.saveUndoInstruction('delS',remember)
    
    def __printStudentsUi(self,st):
        self.tk = Tk()
        self.tk.title("Print students")
        framePrintS = Frame(self.tk)
        framePrintS.pack()
        self.frame = framePrintS
        lbl = Label(framePrintS, text=st)
        lbl.pack(side=TOP)
    
    def __printStudents(self):
        st = ""
        for x in self.__studentCtrl.getAll():
            st += str(x) + "\n"
        self.__printStudentsUi(st)
    
    def __findStudentByIdUi(self):
        self.tk = Tk()
        self.tk.title("Find student")
        frameFindS = Frame(self.tk)
        frameFindS.pack()
        self.frame = frameFindS
        lbl = Label(frameFindS, text="ID:")
        lbl.pack(side=LEFT)
        self.idS = Entry(frameFindS, {})
        self.idS.pack(side=LEFT)
        self.ctrlFindSBtn = Button(frameFindS,text="Find it",command = self.__findStudentById)
        self.ctrlFindSBtn.pack(side=BOTTOM)
    
    def __findStudentById(self):
        try:
            student = self.__studentCtrl.getById(int(self.idS.get()))
            messagebox.showinfo('Look a title',student)
        except studentValidatorException as ex:
            messagebox.showerror('Student Validator Exception', ex)
        except studentRepositoryException as ex:
            messagebox.showerror('Student Repository Exception', ex)
        except Exception as ex:
            messagebox.showerror('Error', ex)
    
    def __assignAssigmentUi(self):
        self.tk = Tk()
        self.tk.title("Assign Assignments")
        frameAssignAssigments = Frame(self.tk)
        frameAssignAssigments.pack()
        self.frame = frameAssignAssigments
        lbl = Label(frameAssignAssigments, text="Assigment ID:")
        lbl.pack(side=LEFT)
        self.idA = Entry(frameAssignAssigments, {})
        self.idA.pack(side=LEFT)
        lbl = Label(frameAssignAssigments, text="Student ID:")
        lbl.pack(side=LEFT)
        self.idS = Entry(frameAssignAssigments, {})
        self.idS.pack(side=LEFT)
        lbl = Label(frameAssignAssigments, text="Group:")
        lbl.pack(side=LEFT)
        self.groupS = Entry(frameAssignAssigments, {})
        self.groupS.pack(side=LEFT)
        self.ctrlAssignToSBtn = Button(frameAssignAssigments,text="Assign to student",command = self.__assignToStudent)
        self.ctrlAssignToSBtn.pack(side=BOTTOM)
        self.ctrlAssignToGBtn = Button(frameAssignAssigments,text="Assign to group",command = self.__assignToGroup)
        self.ctrlAssignToGBtn.pack(side=BOTTOM)
    
    def __assignToStudent(self):
        try:
            assigmentId = int(self.idA.get())
            studentId = int(self.idS.get())
            self.__gradeCtrl.assignAssgiment(assigmentId,studentId)
            grade = gradeDomain(assigmentId,studentId,0)
            self.__undoRedoCtrl.saveUndoInstruction('addAFS',grade)
            messagebox.showinfo('Succes', 'Done !')
        except studentValidatorException as ex:
            messagebox.showerror('Student Validator Exception', ex)
        except studentRepositoryException as ex:
            messagebox.showerror('Student Repository Exception', ex)
        except assigmentValidatorException as ex:
            messagebox.showerror('Assigment Validator Exception', ex)
        except assigmentRepositoryException as ex:
            messagebox.showerror('Assigment Repository Exception', ex)
        except Exception as ex:
            messagebox.showerror('Error', ex)
    
    def __assignToGroup(self):
        try:
            assigmentId = int(self.idA.get())
            group = int(self.groupS.get())
            self.__gradeCtrl.assignAssigmentGroup(assigmentId,group)
            self.__undoRedoCtrl.saveUndoInstruction('addASG',[assigmentId,group])
            messagebox.showinfo('Succes', 'Done !')
        except studentValidatorException as ex:
            messagebox.showerror('Student Validator Exception', ex)
        except studentRepositoryException as ex:
            messagebox.showerror('Student Repository Exception', ex)
        except assigmentValidatorException as ex:
            messagebox.showerror('Assigment Validator Exception', ex)
        except assigmentRepositoryException as ex:
            messagebox.showerror('Assigment Repository Exception', ex)
        except Exception as ex:
            messagebox.showerror('Error', ex)
    
    def __gradeAStudentUi(self):
        self.tk = Tk()
        self.tk.title("Grade students")
        frameGrade = Frame(self.tk)
        frameGrade.pack()
        self.frame = frameGrade
        lbl = Label(frameGrade, text="Student ID:")
        lbl.pack(side=LEFT)
        self.idS = Entry(frameGrade, {})
        self.idS.pack(side=LEFT)
        self.ctrlShowAvalibleABtn = Button(frameGrade,text="Show avalible assigments",command = self.__showAvalibleAssigments)
        self.ctrlShowAvalibleABtn.pack(side=BOTTOM)
        
    def __showAvalibleAssigments(self):
        try:
            studentId = int(self.idS.get())
            toPrint = self.__gradeCtrl.getAssigments(studentId)
            self.__showAvalibleAssigmentsUi(toPrint)
        except studentValidatorException as ex:
            messagebox.showerror('Student Validator Exception', ex)
        except studentRepositoryException as ex:
            messagebox.showerror('Student Repository Exception', ex)
        except Exception as ex:
            messagebox.showerror('Error', ex)
        #for i in range(len(toPrint)):
        #    aux=str(i+1)
        #    print(aux + '.' + 'Assigment number ' + str(toPrint[i][0]))
        
    def __showAvalibleAssigmentsUi(self,toPrint):
        if toPrint==[]:
            messagebox.showinfo('Nothing found', 'There are no assigments to this student')
        else:
            self.tk = Tk()
            self.tk.title("Avalible assigment to grade")
            frameAvalibleAssigment = Frame(self.tk)
            frameAvalibleAssigment.pack()
            self.frame = frameAvalibleAssigment
            i=0
            for x in toPrint:
                i+=1
                lbl = Label(frameAvalibleAssigment,text='Assigment '+str(x[0]))
                lbl.pack(side=TOP)
            lbl = Label(frameAvalibleAssigment, text="Choice :")
            lbl.pack(side=LEFT)
            self.choice = Entry(frameAvalibleAssigment, {})
            self.choice.pack(side=LEFT)
            lbl = Label(frameAvalibleAssigment, text="Grade :")
            lbl.pack(side=LEFT)
            self.gradeS = Entry(frameAvalibleAssigment, {})
            self.gradeS.pack(side=LEFT)
            self.ctrlGradeStudentBtn = Button(frameAvalibleAssigment,text="Grade him/her/apache helicopter",command = self.__gradeAStudent)
            self.ctrlGradeStudentBtn.pack(side=BOTTOM)
        
    
    def __gradeAStudent(self):
        try:
            x=self.__gradeCtrl.getById(int(self.choice.get()),int(self.idS.get()))
            grade = int(self.gradeS.get())
            self.__gradeCtrl.updateGrade(x.assigmentId,x.studentId,grade)
            gradeD = gradeDomain(x.assigmentId,x.studentId,0)
            gradeD0 = gradeDomain(x.assigmentId,x.studentId,grade)
            self.__undoRedoCtrl.saveUndoInstruction('updG',[gradeD,gradeD0])
            messagebox.showinfo('Succes', 'Done !')
        except studentValidatorException as ex:
            messagebox.showerror('Student Validator Exception', ex)
        except studentRepositoryException as ex:
            messagebox.showerror('Student Repository Exception', ex)
        except assigmentValidatorException as ex:
            messagebox.showerror('Assigment Validator Exception', ex)
        except assigmentRepositoryException as ex:
            messagebox.showerror('Assigment Repository Exception', ex)
        except Exception as ex:
            messagebox.showerror('Error', ex)
    
    def __statisticsUi(self):
        self.tk = Tk()
        self.tk.title("Statistics")
        frameStatistics = Frame(self.tk)
        frameStatistics.pack()
        self.frame = frameStatistics
        self.ctrlStatistics1 = Button(frameStatistics,text="Order students alphabeticaly by an assigment",command = self.__orderStudentsAlphabeticaly)
        self.ctrlStatistics1.pack(side=TOP)
        self.ctrlStatistics2 = Button(frameStatistics,text="Order students with a grade by an assigment",command = self.__orderStudentsByGrade)
        self.ctrlStatistics2.pack(side=TOP)
        self.ctrlStatistics3 = Button(frameStatistics,text="Students that are late in assigment",command = self.__lateStudents)
        self.ctrlStatistics3.pack(side=TOP)
        self.ctrlStatistics4 = Button(frameStatistics,text="Students with best school situation",command = self.__schoolSituation)
        self.ctrlStatistics4.pack(side=TOP)
        self.ctrlStatistics5 = Button(frameStatistics,text="Grades from an assigment",command = self.__assigmentGrades)
        self.ctrlStatistics5.pack(side=TOP)
        lbl = Label(frameStatistics, text="Assigment Id (just in case) :")
        lbl.pack(side=LEFT)
        self.idA = Entry(frameStatistics, {})
        self.idA.pack(side=LEFT)
        
    def __assigmentGradesUi(self,toGive):
        self.tk = Tk()
        self.tk.title("Assigment Grades")
        frameAssigmentGrades = Frame(self.tk)
        frameAssigmentGrades.pack()
        self.frame = frameAssigmentGrades
        for x in toGive:
            lbl = Label(frameAssigmentGrades, text=str(x[0])+' '+str(x[1]))
            lbl.pack(side=TOP)
        
    def __assigmentGrades(self):
        try:
            toGive=[]
            assigmentId = int(self.idA.get())
            students = self.__gradeCtrl.assigmentGrades(assigmentId)
            for x in students:
                toGive.append((self.__studentCtrl.getById(x[0]),x[1]))
            if toGive==[]:
                messagebox.showerror('Error', 'There are no students')
            else:
                self.__assigmentGradesUi(toGive)
        except studentValidatorException as ex:
            messagebox.showerror('Student Validator Exception', ex)
        except studentRepositoryException as ex:
            messagebox.showerror('Student Repository Exception', ex)
        except assigmentValidatorException as ex:
            messagebox.showerror('Assigment Validator Exception', ex)
        except assigmentRepositoryException as ex:
            messagebox.showerror('Assigment Repository Exception', ex)
        except ValueError:
            messagebox.showerror('Error','You have to write down the assigment Id !')
        except Exception as ex:
            messagebox.showerror('Error', ex)
        
    def __schoolSituationUi(self,toGive):
        self.tk = Tk()
        self.tk.title("School Situation")
        frameSchoolSituation = Frame(self.tk)
        frameSchoolSituation.pack()
        self.frame = frameSchoolSituation
        for x in toGive:
            lbl = Label(frameSchoolSituation, text=str(x[0])+' '+x[1]+' '+str(x[2]))
            lbl.pack(side=TOP)
    
    def __schoolSituation(self):
        try:
            toGive=[]
            studentAndGrade = self.__gradeCtrl.schoolSituation()
            if studentAndGrade==[]:
                messagebox.showerror('Error', 'There is no school situation')
            else:
                for x in studentAndGrade:
                    toGive.append((self.__studentCtrl.getById(x[0]), ' with grade ',x[1]))
                self.__schoolSituationUi(toGive)
        except studentValidatorException as ex:
            messagebox.showerror('Student Validator Exception', ex)
        except studentRepositoryException as ex:
            messagebox.showerror('Student Repository Exception', ex)
        except assigmentValidatorException as ex:
            messagebox.showerror('Assigment Validator Exception', ex)
        except assigmentRepositoryException as ex:
            messagebox.showerror('Assigment Repository Exception', ex)
        except ValueError:
            messagebox.showerror('Error','You have to write down the assigment Id !')
        except Exception as ex:
            messagebox.showerror('Error', ex)
            
    def __lateStudentsUi(self,toGive):
        self.tk = Tk()
        self.tk.title("Late Students")
        frameLateStudents = Frame(self.tk)
        frameLateStudents.pack()
        self.frame = frameLateStudents
        for x in toGive:
            lbl = Label(frameLateStudents, text=str(x))
            lbl.pack(side=TOP)
    
    def __lateStudents(self):
        try:
            toGive=[]
            toPrint = self.__gradeCtrl.lateStudents()
            for x in toPrint:
                toGive.append(self.__studentCtrl.getById(x))
            if toGive==[]:
                messagebox.showerror('Error', 'There are no students')
            else:
                self.__lateStudentsUi(toGive)
        except studentValidatorException as ex:
            messagebox.showerror('Student Validator Exception', ex)
        except studentRepositoryException as ex:
            messagebox.showerror('Student Repository Exception', ex)
        except assigmentValidatorException as ex:
            messagebox.showerror('Assigment Validator Exception', ex)
        except assigmentRepositoryException as ex:
            messagebox.showerror('Assigment Repository Exception', ex)
        except ValueError:
            messagebox.showerror('Error','You have to write down the assigment Id !')
        except Exception as ex:
            messagebox.showerror('Error', ex)
            
    def __orderStudentsAlphabeticalyUi(self,toGive):
        self.tk = Tk()
        self.tk.title("Order Students Alphabeticaly")
        frameOSA = Frame(self.tk)
        frameOSA.pack()
        self.frame = frameOSA
        for x in toGive:
            lbl = Label(frameOSA, text=str(x))
            lbl.pack(side=TOP)       
            
    def __orderStudentsAlphabeticaly(self):
        try:
            assigmentId = int(self.idA.get())
            studentIdList = self.__gradeCtrl.getStudents(assigmentId)
            students = []
            for x in studentIdList:
                students.append(self.__studentCtrl.getById(int(x[0])))
            students = sorted(students,key = lambda student: student.name)
            toGive=[]
            for x in students:
                toGive.append(x)
            if toGive==[]:
                messagebox.showerror('Error', 'There are no students')
            else:
                self.__orderStudentsAlphabeticalyUi(toGive)
        except studentValidatorException as ex:
            messagebox.showerror('Student Validator Exception', ex)
        except studentRepositoryException as ex:
            messagebox.showerror('Student Repository Exception', ex)
        except assigmentValidatorException as ex:
            messagebox.showerror('Assigment Validator Exception', ex)
        except assigmentRepositoryException as ex:
            messagebox.showerror('Assigment Repository Exception', ex)
        except ValueError:
            messagebox.showerror('Error','You have to write down the assigment Id !')
        except Exception as ex:
            messagebox.showerror('Error', ex)
        
    def __orderStudentsByGradeUi(self,toGive):
        self.tk = Tk()
        self.tk.title("Order Students By Grade")
        frameOSBG = Frame(self.tk)
        frameOSBG.pack()
        self.frame = frameOSBG
        for x in toGive:
            lbl = Label(frameOSBG, text=str(x[0])+' '+x[1]+' with grade '+str(x[2]))
            lbl.pack(side=TOP)     
    
    def __orderStudentsByGrade(self):
        try:
            assigmentId = int(self.idA.get())
            studentIdList = self.__gradeCtrl.getStudentsWithGrade(assigmentId)
            studentIdList = sorted(studentIdList, key = lambda student: student[1],reverse = True)
            students = []
            for x in studentIdList:
                students.append(self.__studentCtrl.getById(int(x[0])))
            toGive=[]
            for i in range(len(students)):
                toGive.append((students[i] , ' with grade ' , studentIdList[i][1]))
            if toGive==[]:
                messagebox.showerror('Error', 'There are no students')
            else:
                self.__orderStudentsByGradeUi(toGive)
        except studentValidatorException as ex:
            messagebox.showerror('Student Validator Exception', ex)
        except studentRepositoryException as ex:
            messagebox.showerror('Student Repository Exception', ex)
        except assigmentValidatorException as ex:
            messagebox.showerror('Assigment Validator Exception', ex)
        except assigmentRepositoryException as ex:
            messagebox.showerror('Assigment Repository Exception', ex)
        except ValueError:
            messagebox.showerror('Error','You have to write down the assigment Id !')
        except Exception as ex:
            messagebox.showerror('Error', ex)
    
    def __undoUi(self):
        try:
            self.__undoRedoCtrl.doTheUndo()
            messagebox.showinfo('Succes', 'Done !')
        except undoRedoValidatorException as ex:
            messagebox.showerror('Undo/Redo Validator Exception', ex)
        except Exception as ex:
            messagebox.showerror('Error', ex)
    
    def __redoUi(self):
        try:
            self.__undoRedoCtrl.doTheRedo()
            messagebox.showinfo('Succes', 'Done !')
        except undoRedoValidatorException as ex:
            messagebox.showerror('Undo/Redo Validator Exception', ex)
        except Exception as ex:
            messagebox.showerror('Error', ex)
            
    
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