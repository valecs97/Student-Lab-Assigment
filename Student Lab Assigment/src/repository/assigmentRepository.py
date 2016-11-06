'''
Created on Nov 2, 2016

@author: Vitoc
'''

from validator.valid import assigmentRepositoryException
from domain.assigmentDomain import assigmentDomain

class assigmentRepository:


    def __init__(self):
        self.__assigments={}
        
    '''
    Function that adds the assigment to the repository
    
    input data :
    toAdd - assigmentDomain
    
    Raise assigmentRepositoryException if :
    1.The id already exists
    '''
        
    def addAssigment(self,toAdd):
        if toAdd.assigmentId in self.__assigments:
            raise assigmentRepositoryException('Invalid ID!')
        self.__assigments[toAdd.assigmentId]=toAdd
    
    '''
    Function that updates the assigment in the repository
    
    input data :
    toUpdate - assigmentDomain
    
    Raise assigmentRepositoryException if :
    1.The id doesnt exist
    '''
    
    def updateAssigment(self,toUpdate):
        if toUpdate.assigmentId not in self.__assigments:
            raise assigmentRepositoryException('Invalid ID!')
        self.__assigments[toUpdate.assigmentId]=toUpdate
        
        
    '''
    def removeAssigment(self,toRemove):
        if toRemove.assigmentId not in self.__assigments:
            raise assigmentRepositoryException('Invalid ID!')
        del self.__assigments[toRemove.assigmentId]
    '''
    
    '''
    Function that removes the assigment from the repository
    
    input data :
    toDelete - integer
    
    Raise assigmentRepositoryException if :
    1.The id doesnt exist
    '''
    
    def removeAssigmentById(self,toRemove):
        if toRemove not in self.__assigments:
            raise assigmentRepositoryException('Invalid ID!')
        del self.__assigments[toRemove]
    
    '''
    Function that finds an assigment in the repository
    
    input data :
    toFind - integer
    
    output data :
    assigmentDomain
    
    Raise assigmentRepositoryException if :
    1.The id doesnt exist
    '''
    
    def findById(self,toFind):
        if toFind not in self.__assigments:
            raise assigmentRepositoryException('Invalid ID!')
        return self.__assigments[toFind]
        
    '''
    Function that removes the assigment from the repository
    
    input data :
    toDelete - assigmentDomain
    
    output data:
    a list of assigmentDomain
    
    Raise assigmentRepositoryException if :
    1.The id doesnt exist
    '''
        
    def getAll(self):
        l=[]
        for i in self.__assigments.values():
            l.append(i)
        return l
    
    '''
    Function that helps the controller to call the function easier
    '''
    
    def __add__(self,toAdd):
        self.addAssigment(toAdd)
        
    def __radd__(self,toAdd):
        self.addAssigment(toAdd)
        
    def __sub__(self,toRemove):
        if type(toRemove) is int:
            self.removeAssigmentById(toRemove)    
        if type(toRemove) is assigmentDomain:
            self.removeAssigment(toRemove)
                
    def __rsub__(self,toRemove):
        self.__sub__(toRemove)  
        
    def __getitem__(self,toFind):
        return self.findById(toFind)          
    
    def __len__(self):
        return len(self.__assigments)
    
    def __str__(self):
        st = ""
        for x in self.__assigments.values():
            st += str(x)+"\n"
        return st
