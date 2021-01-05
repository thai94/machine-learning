def helloWorld(name):
    print "Hello: %s" % name
    return

helloWorld("Thai")

def changeme(myList) :
    myList.append([1,2,3,4]);
    print "After change: ", myList
    return
def changeme2(myList) :
    myList = [1,2,3,4];
    print "After change: 2", myList
    return

myList = [10, 20, 40]
changeme(myList)
print myList
changeme2(myList)
print myList

def printInfo(name, age = 20) :
    print "Name: ", name
    print "Age: ", age
    return

printInfo("Thai")