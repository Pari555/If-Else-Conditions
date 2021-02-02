## If/Elif/Else Conditional Statements
Used for desision-making operations with conditions

Conditional statements always start with an 
`if` header
`elif` is optional, but we can use as many as we want
`else` is optional, but only 1 for every `if`

### Condition:
An expression that evaluates to produce a a result which is a Boolean value (AKA. Boolean expression)

### Indentation:
Python relies on indentation to define scope in the code

### Formula:
if (Condition):
> Body Statement

elif (Condition):
> Body Statement

else: 
> Body Statement

*Ex.*
```
a = 2
if (a == 0):
    print("hi")
else:
    print("bye")
```
> bye

## Nested Conditional Statements

A Conditional statement inside another conditional statement

## Indentation

The header/clause of a nested conditional statement must be indented from an outer header.

## Formula

```
if(Condition):
  if(Condition): <---- Starting a nested statement
   Body Statement
  elif(Condition):
   Body Statement
  else:
   Body Statement <---- End of nested statement.
elif(Condition):
  Body Statement
else:
  Body Statement
```

*Ex.*

```
x = 10
y = 10
if (x < y):
  print("x is less than y")
else:
  if(x > y):
  print("x is greater than y")
  else:
   print("x and y must be equal")
```
> x and y must be equal

## Order of Operations

1. () Parentheses
2. ** Exponents
3. -a,+a Negative, Positive arguements
4. *, /, //, % Multiplication, Division, Quotient, Modulus
5. +, - Addition, Subtraction
6. <, <=, >, >=, ==, != Comparison Operators
7. not Boolean Not
8. and Boolean And
9. or Boolean Or

a++ ----> a = a + 1
a-- ----> a = a - 1