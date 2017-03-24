##################
# Built-in Lists #
##################

# Initialize
peoples = ["Mao", "Chou", "Liu"]
print peoples
print peoples[0] # >> First Element: "Mao"
print peoples[-1] # >> Last Element: "Liu"
print len(peoples) # >> 3

# Everything fits
jianguo = [1949, "Beijing", "China", peoples]
print jianguo

# Add Element
peoples.append("Lin")
print peoples

jianguo.insert(0, "TianAnMen")
print jianguo

# Change Element
for i in range(0,4):
    peoples[i] = "Famous - " + peoples[i]
print peoples
print jianguo

# Remove Element
del peoples[2]
print peoples # >> ['Famous - Mao', 'Famous - Chou', 'Famous - Lin']

peoples.remove("Famous - Lin")
print peoples # >> ['Famous - Mao', 'Famous - Chou']

jianguo.remove(peoples)
print jianguo

# Concatenate Lists
jianguo.extend(peoples)
print jianguo # >> ['TianAnMen', 1949, 'Beijing', 'China', 'Famous - Mao', 'Famous - Chou']

# Slicing List
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

firstTwo = squares[0:2]
print firstTwo # >> [0, 1]

lastTwo = squares[-2:]
print lastTwo # >> [0, 1]

exceptFirst = squares[1:]
print exceptFirst

exceptLast = squares[:-1]
print exceptLast

# enumerate() for index
days = ["Mon", "Tues", "Wed", "Thr", "Fri", "Sat", "Sun"]
for i, d in enumerate(days):
    print  i, d



#########################
# Built-in Dictionaries #
#########################
# Initialize and Access
capitals = {'Peru':'Lima', 'China': 'Beijing', 'US':'Washington', 'Italy':'Rome', 'Germany':'Berlin', 'India':'Dehli'}
print capitals['China'] # >> Beijing
print 'Italy' in capitals # >> True

# Concatenating without Collision
moreCapitals = {'Japan': 'Tokyo', 'Korea': 'Seoul', 'India':'Delhi'}
capitals.update(moreCapitals)
print capitals['India'] # >> Delhi

# Iterations
for key in capitals.keys():
    key = "Capital of " + key
print capitals

for value in capitals.values():
    value = value + " 2017"
print capitals

for key, value in capitals.items():
    print key + " - " + value


##################
# Comprehensions #
##################
# For Lists
square3 = [i**2 for i in range(30) if i % 3 == 0]
print square3

# For Dictionaries
square4 = {i: i**2 for i in range(30) if i % 4 == 0}
print square4

# Transform Dictionary
capitalsByCap = {capitals[key]: key for key in capitals}
print capitalsByCap