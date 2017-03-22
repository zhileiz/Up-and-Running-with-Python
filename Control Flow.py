################
# Conditionals #
################
# Basic Conditional
def compare(x, y):
    if (x < y):
        str = "x is less than y"
    elif (x == y):
        str = "x is equal to y"
    else:
        str = "x is larger than y"
    return str

print compare(x = 10, y = 10) # >> x is less than y
print compare(x = 10, y = 15) # >> x is equal to y
print compare(x = 15, y = 10) # >> x is larger than y

# Conditional Statement
def newCompare(x , y):
    st = "x is less than y" if (x < y) else "x is greater than or equal to y"
    return st

print newCompare(5,20)


#########
# Loops #
#########
# Basic While Loop
m = 0
while (m < 5):
    print m
    m = m+1

# Basic For Loop
for x in range(5,10):
    print x

# Loop over Collection
alphabet = ["a", "b", "c", "d"]
for char in alphabet:
    print char

# Break and Continue Statement
for x in range (5,10):
    if (x == 9): break
    if (x % 2 == 0): continue
    print x # >> 5, 7

# enumerate() for index
days = ["Mon", "Tues", "Wed", "Thr", "Fri", "Sat", "Sun"]
for i, d in enumerate(days):
    print  i, d