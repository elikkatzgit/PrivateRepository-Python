import Django

print("Hello World")
Age = 5
Real_age = 5.2
Male = True
Age = 6

# This is a comment

addition = 4 + 5
modulo = 7 % 3

add_assign = 5
add_assign +=7
print(add_assign)

aaa = 15 / 3 * 2 * 2 - (3 + 4)
print(aaa)

print(2019)
print(True)
print ((4 + 5) * 3)

calc = 1.2222 + 3.3333
print(calc)
print(round(calc, 3))
print(round(calc, 2))

example_string = 'This is .  strings'
example_string = "This is . strings"

example_string = "0123456" #index numbers
example_string = "Orange"
example_string[2]
print(example_string[2])
print("apple"[4])

print("apicots")
print("apricots"[:3])
print("apricots"[2:5])
print("apricots"[4:])

print("pecan" + " " + "pie")

concat = "R2" + "-" + "D2"
print(concat)
print(concat[3])
print(concat[1:4])

unchanged = "forrest Gump"
slices = unchanged[6:]
print(unchanged)
print(slices)
print(unchanged[10])

ex_3 = False
ex_4 = 29
ex_5 = 3.2343
print(type(ex_3))
print(type(ex_4))
print(type(ex_5))

ex_3 = str(False)
ex_4 = str(29)
ex_5 = str(3.2343)
print(type(ex_3))
print(type(ex_4))
print(type(ex_5))

print("This\tis\ta\lot")
print("First line\nsecond line")
print("there is only one backslash \\")


#name = input("Please enter your name.")
#print("Your name is " + name + ".")
#print(type(name))

#magic = int(input("Choose a number."))
#print("magic")
#print(type(magic))

#Functions

print("this")
print("is")
print("it")
print("this")
print("is")
print("it")
print("this")
print("is")
print("it")

def prints_three():
    print("this")
    print("is")
    print("it")

prints_three()

print("===============")

def function_name(parameter):
    print(parameter + 2)


function_name(8)

first_str = "The number "

def function_name1(p1, p2, p3):
    print(p1 + str(p2) + p3)


function_name1(first_str, 5, " Is an integer.")

def default_example(num1=7, num2 =8):
    print(num1 * num2)


default_example()
default_example(2)
default_example(2, 5)

#return

def default_example(num1=7, num2 =8):
    return num1 * num2

print(default_example() + 44)

#imports

import random
print(random.randint(1,10))

#function import

from random import randint
print(randint(10,20))

#universal import

from random import *
print(random())

# flows
print("==== Flows ====")
print(4 > 2)
print(4 > 6)
print(10 != 100)
print(10 == 10)
print("Hello" == "Hello")
print("Hello" == "hello")

print(4 == 4 and "Elik" == "Elik")
print(4 == 4 or "Elik" == "Katz")

#if
#print("==== If staatments ====")
# veg = input("Type a name of a veggie.")

#if veg == "corn":
#    print("The veggie is corn")
#else:
#    print("You didnt choose corn.")


print("======IF and ELSE ===========")
print("Let's do a magic now")
#number = int(input("Please choose a number between 1 - 10 : "))
number = int(3)
import random
magic = random.randint(1,10)
print("I was thinking of the number" ,magic)

if number != magic:
    print("Bommer! You choose", number ,"and I choose" , magic)
else:
    print("WOW !!!! We made it")

print("I will generate a random number...")
magic2 = random.randint(-10,10)
print("The number is [", magic2,"]")
if magic2 < 0:
    print("The number is less then 0.")
elif magic2 == 0:
    print("The number is 0.")
else:
    print("The number is grater then 0")

print(bool(0))
print(bool(400))
print(bool(""))
print(bool("elik"))

print("==== whileLoop =====")

counter = 0
while counter < 3:
    print("I counted", counter)
    counter += 1

print("==== For Loops =====")

word = "house"

for letter in word:
    print(letter)

print("==== Range ====")

one_input = range(5)

for num in one_input:
    print(num)

print("-----")
two_inputs = range(5, 10)
for num in two_inputs:
    print(num)

print("-----")
three_inputs = range(1, 10, 2)
for num in three_inputs:
    print(num)

print("=== CASES ===")

all_low = "there are no upper case"
print(all_low)
print(all_low.upper())
all_up = "THERE IS NO LOWER CASE"
print(all_up)
print(all_up.lower())

print("MixedCase".isupper())
print("ALLUPCASE".isupper())
print("alllo\"wer".islower())
print("HELP!".lower())
print("Elik-Katz".isalpha())
print("054-2124779".isdecimal())

print("this is a string".startswith("This"))

print("-".join(["Elik","Katz","Belik"]))
print(",".join(["Elik","Katz","Belik"]))

print("egg,  milk,water".split())
print("egg,  milk,water".split(","))

print("HelloWorld!".rjust(15)) #Adding spaces to total 15 char
print("HelloWorld!".ljust(15), "END") #Adding spaces to end
print("HelloWorld!".rjust(15,"*"))
print("HelloWorld!".center(15,"*"))
print("HelloWorld!!!!!!".strip("!"))
print("HelloWorld!!!!!!".rstrip("!"))
print("HelloWorld!!!!!!".lstrip("Hello"))

print("!!!!!!!HelloWorld!!!!!!".strip("!"))

print("**!!**HelloWorld!!!!!!".replace("!","*"))

print(len("**!!**HelloWorld!!!!!!"))
