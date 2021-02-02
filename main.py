a = 200
b = 33

if (b > a):
  print("b is greater than a")
else:
  print("b is not greater than a")

 # Write a conditional statement that evaluates if the user input is positive or negative.

a = 5000 # Hard Coding
Num = int(input("Choose a number?"))

if (Num > 0):
   print("This number is positive")
elif (Num == 0):
   print("You entered 0")
else:
   print("The number is negative")

# Ask the user for their age
# If they are younger than 13 they can only watch PG/G movies
# If they are 13 and older but younger than 17, they can only watch PG/13/PG/G movies
# If they are 17 and older, they can watch all movies

age = int(input("What is your age?"))

if (age < 13):
  print("You can only watch PG/G movies")
elif (17 > age >= 13):
  print("You can only watch PG/13/PG/G movies")
else:
  print("You can watch all movies")
     
is_Hungry = True
is_Sleepy = False
is_Bored  = True
if (is_Hungry == True):
  print("You should go eat")
if (is_Sleepy == True):
  print("You should go sleep")
if (is_Sleepy == False):
  print("You are well rested")


if (is_Hungry == is_Bored or is_Sleepy == is_Hungry):
  print("You should do your homework")
else:
  print("You can play outside.")

if (is_Sleepy == is_Hungry and is_Hungry == is_Bored):
   if(is_Sleepy == is_Bored):
     print("it's nap time")
else:
   print("it's time for bed")

# Asks the user for a number
# Tells the user if the number is even or odd

question = int(input("Choose a number : "))

if (question % 2 != 0):
   print("This number is odd")
else:
   print("The number is even")

# Math Quandants
# Ask the user for a x and y value
# Using a nested conditional, output which quadrant they are in

x = int(input("Choose a value for x :"))
y = int(input("Choose a value for y :"))

if ( x > 0 ):
  if ( y > 0 ):
    print("You're number is in the first quadrant")
  else:
    print("You're number is in the fourth quadrant")
elif (x < 0):
  if ( y < 0 ):
    print("You're number is in the third quadrant")
  if ( y > 0 ):
    print("You're number is in the second quadrant")

# create an if statement using 'and' or 'or' for the third and second quadrant
if( x < 0 and y > 0 ):
  print("You're number is in the second quadrant")
elif ( x < 0 and y < 0 ):
  print("You're number is in the third quadrant")

# let the user know if they are on the x-axis or y-axis
# if we have +y or -y but x == 0
# "You are on the y-axis"
# if we have +x or -x but y == 0
# "You are on the x-axis"

if( x == 0 and y != 0 ):
  print("You are on the y-axis")
if( y == 0 and x != 0 ):
  print("You are on the x-axis")

# if x and y are 0, output the origin 
if(x == 0 and y == 0):
    print("You are on the origin")

# and, or 
# and takes precedence over or
# 'and' both conditions have to be correct
# 'or' only one condition has to be correct

x = 5
y = 6
z = 7
if( x == 5 and y == 5 or z == 5 ):
  print("Yay")
else:
  print("Nay")

if( x == 5 or y == 5 and z == 5):
  print("Yay")
else:
  print("Nay")
