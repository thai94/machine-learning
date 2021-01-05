class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

class Child(Parent):
    __hideAttr = 200
    def __init__(self):
        print "Calling child contructor"
    def childMethod(self):
        print "Parrent attr: ", self.parentAttr
        print "Calling child method"
        print "Hide attr: ", self.__hideAttr
        self.__hideMethod()
    def __hideMethod(self):
        return

ch = Child()
ch.childMethod()
ch.parentMethod();