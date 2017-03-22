###################
# INTRO TO PYTHON #
###################
# Hello World
print "Hello World"

# Hello World in a function
def main():
    print "hello World"

if __name__ == '__main__':
    main()


#############
# Variables #
#############
#  Declare a Variable and Initialize it
f = 0
print f

# Redeclare variable
f = "abc"
print f
del f

# Different Types cannot be combined
# print "this: " + 123 does not work, you must do:
print "Number: " + str(123)

# Local and Global Variables
f = 0
def localFunction():
    f = "def"
    print f

localFunction() # >> "def"
print f # >> 0

def globalFunction():
    global f
    f = "fed"
    print f

globalFunction()  # >> "def"
print f  # >> 0
del f



##########################
# Working with Functions #
##########################
# Basic Function Property
def func1():
    print "I am a function"

func1() # >> "I am a function"
print func1() # >> "I am a function \nNone"
print func1 # >> <function hash>

def func2(arg1, arg2):
    print arg1, " ", arg2

func2("Tom", "Hanks") # >> "Tom Hanks"
print func2("Tom", "Hanks") # >> "Tom Hanks \nNone"
print func2 # >> <function hash>

# function returning a value
def cube(x):
    return x*x*x

print "Cube of 3 is: " + str(cube(3))

# function with default argument value
def power (num, x=1):
    result = 1;
    for i in range(x):
        result = result * num
    return result

print power(2) # >> 2
print power(2,3) # >> 8
print power(x=3, num=2) # >> 8

# function with variable number of arguments
def multi_add(*args):
    result = 0;
    for x in args:
        result = result + x
    return result

print multi_add(1,2,3,4,5) # >> 15