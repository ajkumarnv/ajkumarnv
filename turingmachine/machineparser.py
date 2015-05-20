##############################################################################
# Author: Ajay Kumar
# Email : simplyajay@gmail.com
##############################################################################

class MachineParser:
    """ This class parses the input file and keeps inputs for the
        turing Machine definition and Tape Definition
    """
    def __init__(self,inputFile=""):
        self.__actionTable = {}
        self.____inputTapeStr = ""
        self.__tapeStartIndex =None
        self.__startStateIndex = None
        self.__haltStateIndex = None
        try:
            sock = open(inputFile,'r')
            self.__parse(sock)
            sock.close()
        except(IOError):
            print "Unable to Open Machine definition File %s" %(inputFile,)
            

    def __parse(self,sock):
        
        self.__inputTapeStr = sock.readline().strip()
        #print "Input Tape Str is :%s" %(self.__inputTapeStr)
        
        self.__tapeStartIndex = int(sock.readline().strip())
        #print "Tape Start Index is :%d"%(self.__tapeStartIndex)

        self.__startStateIndex = int(sock.readline().strip())
        #print "Start State Index is :%d"%(self.__startStateIndex)
    
        self.__haltStateIndex = int(sock.readline().strip())
        #print "Halt State Index is :%d"%(self.__haltStateIndex)

        self.__parseActionTable(sock)

    def __parseActionTable(self,sock):
        for tableEntry in sock.xreadlines():
            tableEntry = tableEntry.strip()
            (state,readChar,writeChar,direction,nextState)=tableEntry.split()
            #print state,readChar,writeChar,direction,nextState
            self.__actionTable[state] = self.__actionTable.get(state,{})
            #print self.__actionTable[state]
            self.__actionTable[state][readChar]=(writeChar,direction,int(nextState))


    def getActionTable(self):
        return self.__actionTable

    def getTapeData(self):
        return self.__inputTapeStr

    def getStartIndex(self):
        return self.__tapeStartIndex

    def getStartState(self):
        return self.__startStateIndex

    def getHaltState(self):
        return self.__haltStateIndex

    def getValidStates(self):
        return map (int, self.__actionTable.keys() )

if __name__=="__main__":
    mp = MachineParser('coho.txt123')
    print "Possible Active states are:"
    for key in mp.getActionTable().keys():
        print key 
        tmpDict = mp.getActionTable()[key]
        for read,value in tmpDict.iteritems():
            print read ,type(value),value

