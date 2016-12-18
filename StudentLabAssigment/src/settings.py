'''
Created on Dec 11, 2016

@author: Vitoc
'''


class settings:

    def __init__(self, filename):
        self.__filename=filename
        
    def examineTheFile(self):
        try:
            with open(self.__filename) as f:
                content = f.readlines()
                loc = content[0].index('=')
                loc+=1
                content[0]=content[0][loc:]
                if content[0]=='inmemory\n':
                    return self.inMemoryRepository(content[1:])
                elif content[0]=='textfiles\n':
                    return self.textFileRepository(content[1:])
                elif content[0]=='binaryfiles\n':
                    return self.binaryFileRepository(content[1:])
                else:
                    raise IOError
        except IOError:
            print("No settings file found or the type of repository isnt avalible")
            print("Creating the default file with in memory repository\n")
            return self.createInMemorySettings()
        except:
            print("An unhandled error has occured , please review your settings file")
            
    def createInMemorySettings(self):
        f = open(self.__filename,'w+')
        toWrite = 'repository=inmemory\nassigments=""\nstudents=""\ngrades=""'
        f.write(toWrite) 
        f.close()
        return {'repositoryType':'inmemory','assigments':None,'students':None,'grades':None}
                    
    def inMemoryRepository(self,content):
        toReturn = {'repositoryType':'inmemory'}
        for line in content:
            line = self.__readLine(line)
            toReturn[line[0]]=line[1]
        return toReturn
    
    def textFileRepository(self,content):
        toReturn = {'repositoryType':'textfiles'}
        for line in content:
            line = self.__readLine(line)
            toReturn[line[0]]=line[1]
        return toReturn
            
    
    def binaryFileRepository(self,content):
        toReturn = {'repositoryType':'binaryfiles'}
        for line in content:
            line = self.__readLine(line)
            toReturn[line[0]]=line[1]
        return toReturn
        
    def __readLine(self,line):
        loc = line.index('=')
        command = line[:loc]
        loc = line.index('"')
        loc+=1
        line = line[loc:]
        loc=line.index('"')
        line = line[:loc]
        return [command,line]