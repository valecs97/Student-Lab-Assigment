'''
Created on Nov 26, 2016

@author: valec
'''

class commandDomain:

    def __init__(self, instruction,remember):
        self.__instruction = instruction
        self.__remember = remember

    def get_instruction(self):
        return self.__instruction


    def get_remember(self):
        return self.__remember


    def set_instruction(self, value):
        self.__instruction = value


    def set_remember(self, value):
        self.__remember = value


    def del_instruction(self):
        del self.__instruction


    def del_remember(self):
        del self.__remember

    instruction = property(get_instruction, set_instruction, del_instruction, "instruction's docstring")
    remember = property(get_remember, set_remember, del_remember, "remember's docstring")
        
        