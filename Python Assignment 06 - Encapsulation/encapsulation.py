# Simple program on encapsulation


class ProtectedClass:
    def __init__(self): #intialization function, the underscores in "__privateMsg" denotes a private variable
        self.__privateMsg = "This is private"
        self._protectedMsg = "This is protected"

    def getPrivate(self):
        print(self.__privateMsg)

    def setPrivate(self, private):
        self.__privateMsg = private



if __name__ == "__main__":

    #instaniating object and message we will try to overwrite variables with
    obj = ProtectedClass()
    newMsg = "This is the manipulated message"

    """

    The code below will cause an error, because the varible "__privateMsg" is private it cannot be accessed outside of the
    class, the only way to print or manipulate is through class functions, which we do below.
    
    print(obj.__privateMsg)
    obj._privateMsg = newMsg
    print(obj.__privateMsg)
    
    """

    # Using the class functions we can print and manipulate the private variable
    obj.getPrivate()
    obj.setPrivate(newMsg)
    obj.getPrivate()

    # Though _protectedMsg is "protected" manipulating it is quite easy.
    print(obj._protectedMsg)
    obj._protectedMsg = newMsg
    print(obj._protectedMsg)
    
