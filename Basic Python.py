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

# Declare a Variable and Initialize it
f = 0
print f

# Redeclare variable
f = "abc"
print f

# Different Types cannot be combined
# print "this: " + 123 does not work, you must do:
print "Number: " + str(123)