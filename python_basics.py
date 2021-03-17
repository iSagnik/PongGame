# printing
print("Hello world")
print(2 + 3)

print("2" * 6)

#variables
x = 5
y = 'Hi how\'s it going?'
print(x, " ", y)
print( type(y) )

#type function
y = 10
print(y)
print( type(y) )

#multiple assignment
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#strings
word = "excellant"
print(len(word))
print(word[2:])

#operators and conditionals
print(10 > 9)
print(10 == 9)
print(10 < 9)

#lists
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))

list1 = ["abc", 34, True, 40, "male"]
print(list1[0])
print(list1[1])

list1.append("New Item")
print(list1)

list1.remove("abc")
print(list1)

list1.pop(2)
print(list1)

#tuple
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

a = 33
b = 200
if b > a:
  print("b is greater than a")
  
#if-else
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

if a > b: print("a is greater than b")

#and & or
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#loops
i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in range(2, 6):
  print(x)

for x in [0, 1, 2]:
  pass

#functions

def add(x, y):
    return x + y

def is_even(num):
    if num % 2 == 0:
        return True
    return False

def print_email(email = "sagnik@packhacks.com"):
    print(email)