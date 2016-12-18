'''
Created on Nov 2, 2016

@author: Vitoc
'''

class studentDomain:

    '''
    A student domain which stores the id , name and the group
    There are also getters and setters for each object apart
    '''

    def __init__(self,studentId,name,group):
        self.__studentId=studentId
        self.__name=name
        self.__group=group

    def get_student_id(self):
        return self.__studentId


    def get_name(self):
        return self.__name


    def get_group(self):
        return self.__group


    def set_student_id(self, value):
        self.__studentID = value


    def set_name(self, value):
        self.__name = value


    def set_group(self, value):
        self.__group = value


    def del_student_id(self):
        del self.__studentId


    def del_name(self):
        del self.__name


    def del_group(self):
        del self.__group
        
    @staticmethod
    def readStudent(line):
        elems = line.split(',')
        t = studentDomain(int(elems[0]),elems[1],int(elems[2]))
        return t
    
    @staticmethod
    def writeStudent(student):
        return str(student.studentId) + ',' +student.name + ',' + str(student.group)

    def __str__(self):
        return str(self.__studentId) + ' ' + self.__name + ' ' + str(self.__group)
    studentId = property(get_student_id, set_student_id, del_student_id, "studentID's docstring")
    name = property(get_name, set_name, del_name, "name's docstring")
    group = property(get_group, set_group, del_group, "group's docstring") 