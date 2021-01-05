#!/usr/bin/python

str = "Hello world"
print str
print str[0]
print str[0:5]
print str[6:]

list = ["iphone", "BPhone", "Android"]
print list
print list[1]
print list[1:3]

tuples = ("ios", "android")
print tuples

dict = {}
dict[0] = "value one"
dict["two"] = "value two"

print dict
print dict[0]
print dict["two"]

a = 100
b = 26.2
print a // b

isBoy = True
isRich = False
print isBoy and isRich
print not isBoy

print "iphone" in list
print "iphone 12" in list