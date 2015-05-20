###################################################################
# Author : Ajay Kumar
# Email  : simplyajay@gmail.com
###################################################################

from tape import Tape
from machineparser import MachineParser
import sys
class TuringMachine() :
    """ Turing Machine class shall runn the machine
        based on the input data and machine definition
    """
    def __init__(self,
                 tapeObject = None,
                 startState = None,
                 startIndex = 0,
                 haltState = None,
                 stateAction = {},
                 validStates=[]):
        print tapeObject,startState, startIndex, haltState,stateAction,validStates
        self.__tapeObject = tapeObject
        self.__state = startState
        self.__index = startIndex
        self.__haltState = haltState
        self.__stateActions = stateAction
        self.__validStates = validStates


    def run(self):
        if self.__state in self.__validStates:
            print "Tape index: [%s]" %(self.__index)
            print "Machine State: %d" %(int(self.__state))
            readChar = self.__tapeObject[self.__index]
            print "Char under tape head %s" %(readChar)
            try:
                stateTable = self.__stateActions.get(str(self.__state))
                print "State table %s" %(stateTable)
                if readChar in stateTable:
                    (writeChar,direction,nextState) = stateTable[readChar]
                elif '*' in stateTable:
                    (writeChar,direction,nextState) = stateTable['*']

                print (writeChar,direction,nextState)

                if writeChar != "*":
                    self.__tapeObject[self.__index] = writeChar

                self.__index += int(direction)
                self.__state = nextState
                self.dumpTape()
                
                    
            except (keyError):
                print "State %s is have no action table" %(self.__state)
                self.__state = self.__haltState

    def halt(self):
        if self.__state == self.__haltState:
            return True
        else:
            return False
            
            
    def dumpTape(self):
        print self.__tapeObject



if __name__=='__main__':
    try:
        mp = MachineParser(sys.argv[1])
        tape = Tape(mp.getTapeData())
        tm = TuringMachine(tapeObject = tape,
                           startState = mp.getStartState(),
                           startIndex = mp.getStartIndex(),
                           haltState = mp.getHaltState(),
                           stateAction = mp.getActionTable(),
                           validStates = mp.getValidStates())
    except:
        print "Error while creating and running machine"
        exit (-1)

    print "########################################################"
    print tape
    i = 0
    while not tm.halt():
        print "iteration : [%d]" %(i)
        tm.run()
        i += 1 

    

