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
if (is_Hungry == True):
  print("You should go eat")
if (is_Sleepy == True):
  print("You should go sleep")
if (is_Sleepy == False):
  print("You are well rested")

