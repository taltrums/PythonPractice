# Declare a variable and initialize it
a = 0
print (a)

# re-declaring the variable works
a = "abc"
print (a)

# ERROR: variables of different types cannot be combined
#print ("string type " + 123)
print ("string type " + str(123))

# Global vs. local variables in functions
def someFunction():
  #global a
  a = "def"
  print (a)

someFunction()
print (a) 

del a
print (a)
