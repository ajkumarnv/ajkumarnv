################################################################################
#Author:Ajay Kumar
#Description:This turing machine will take an argument of .txt file which shall define the during machine
#       as well as input tape
#
################################################################################

class Tape(object):
    """ This class defines the tape object which keeps the data
        in the form of a dictionary with index as keys and exposing API
        to modify, access and convert it into a string"""
    def __init__(self,inputStr="",blankSymbol="-"):
        self.__tape={}
        for index in range(len(inputStr)):
            self.__tape[index] = inputStr[index]
        self.__blankSymbol = blankSymbol


    def __str__(self):
        """ This function is internally called by the Python to convert
            the tape object inot a string """
        
        return "".join((self.__tape.values()))


    def __getitem__(self,index):
        """Internalled called by python while indexing the Tape"""
        print self.__tape
        if index in self.__tape:
            return self.__tape[index]
        else:
            return self.__blankSymbol

    def __setitem__(self,index,val):
        """This function is internally called by Python"""
        self.__tape[index]=str(val)


if __name__=="__main__":
    tapeObject = Tape("123455666-4555-4",'-')
    print tapeObject
    tapeObject[9]=7
    print tapeObject
