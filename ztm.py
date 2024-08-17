"""Reference script"""

# Operator Precedence

# () - Parenthases
# ** - Exponents
# * / - Multiplication and Division
# + - - Addition and Subtraction

# PEMDAS

print(20 - 3 * 4)  # 8
print((20 - 3) * 4)  # 68
print(20 / 4 * 5)  # 25
print(20 * 4 / 5)  # 16
print(20 // 4 * 5)  # 25
print(20 * 4 // 5)  # 16

# Guess the output of each answer before you click RUN

print((5 + 4) * 10 / 2)
print(((5 + 4) * 10) / 2)
print((5 + 4) * (10 / 2))
print(5 + (4 * 10) / 2)
print(5 + 4 * 10 // 2)

# Complex Data Types

# int - Integer
# float - Floating Point Number
# complex - Complex Number
# bin - Binary Number

print(bin(5))
print(int("0b101", 2))

# Variables

# Variables are ways to store information in our programs.

iq = 190
print(iq)
user_iq = 190
print(user_iq)

# Varialbes can be reassigned

user_age = iq / 4
print(user_age)

# Constants

PI = 3.14

# Dunder Variables

# __

# Augmented Assignment Operator

some_value = 5
some_value += 2
print(some_value)

# Strings

print(type("hi hello there"))
username = "supercoder"
password = "supersecret"
long_string = """
WOW
0 0
---
"""
print(long_string)
first_name = "Jon"
last_name = "Snow"
full_name = first_name + " " + last_name
print(full_name)

# String Concatenation

print("hello" + " Jon")

# Type Conversion

print(type(str(100)))
print(type(int(str(100))))

# Escape Sequence

weather = 'It\'s "kind of" sunny'
print(weather)
weather = '\t It\'s "kind of" sunny'
print(weather)
weather = '\t It\'s "kind of" sunny \n hope you have a good day!'
print(weather)

# Formatted Strings

name = "Johnny"
age = 55

print("Hi " + name + ". You are " + str(age) + " years old.")
print(f"Hi {name}. You are {age} years old.")
print("Hi {}. You are {} years old.".format("Johnny", "55"))
print("Hi {}. You are {} years old.".format(name, age))
print("Hi {1}. You are {0} years old.".format(name, age))
print("Hi {new_name}. You are {age} years old.".format(new_name="Sally", age=100))

# String Indexes

# Indexing is the process of accessing a specific character in a string.
# Indexing starts at 0.
# The first character in a string is at index 0.
# The second character in a string is at index 1.

selfish = "abcdefgh"
#          01234567
print(selfish[0])
print(selfish[7])
print(selfish[4])
print(selfish)

selfish = "01234567"
#          01234567

# [start:stop]
# The stop index is not included in the slice.

print(selfish[0:2])
print(selfish[0:7])
print(selfish[0:8])

# [start:stop:stepover]
# The stepover is the number of characters to skip

print(selfish[0:8:1])
print(selfish[0:8:2])
print(selfish[1:])
print(selfish[:5])
print(selfish[::1])
print(selfish[-1])
print(selfish[-2])
print(selfish[::-1])
print(selfish[::-2])

# Immutability

selfish = "01234567"
# Strings are immutable
# selfish[0] = '8'
# selfish = '8'

# Built-In Functions + Methods

print(len("hello"))
greet = "hello"
print(greet[0 : len(greet)])
quote = "to be or not to be"
print(quote.upper())
print(quote.capitalize())
print(quote.find("be"))
print(quote.replace("be", "me"))
print(quote)

# Booleans

name = "Jon"
is_cool = False
is_cool = True
print(bool(1))
print(bool(0))
print(bool("True"))

# Exercise: Type Conversion

name = "Jon Snow"
age = 50
relationship_status = "single"
relationship_status = "it's complicated"
print(relationship_status)
birth_year = input("what year were you born?")
age = 2023 - int(birth_year)
print(f"your age is: {age}")

# Exercise: Password Checker

username = input("what is your username?")
password = input("what is your password?")
password_length = len(password)
hidden_password = "*" * password_length
print(
    f"{username}, your password, {hidden_password}, is {password_length} letters long"
)

# Lists

li = [1, 2, 3, 4, 5]
li2 = ["a", "b", "c"]
li3 = [1, 2, "a", True]

# Data Structure

amazon_cart = ["notebooks", "sunglasses"]
print(amazon_cart[0])
print(amazon_cart[1])

# List Slicing

amazon_cart = ["notebooks", "sunglasses"]
print(amazon_cart[0:2])
amazon_cart[0] = "laptop"
print(amazon_cart)
new_cart = amazon_cart[:]
new_cart[0] = "gum"
print(new_cart)
print(amazon_cart)

# Matrix

matrix = [[1, 2, 3], [2, 4, 6], [7, 8, 9]]
print(matrix[0][1])

# List Methods

basket = [1, 2, 3, 4, 5]
print(len(basket))

# Adding

basket.append(100)
new_list = basket
print(basket)
print(new_list)
basket.insert(4, 100)
print(basket)
basket.extend([100, 101])
print(basket)

# Removing

basket.pop()
print(basket)
basket.pop(0)
print(basket)
basket.remove(4)
print(basket)
new_list = basket.pop(4)
print(new_list)
basket.clear()
print(basket)

# Index

basket = ["a", "b", "c", "d", "e"]
print(basket.index("d"))
print("d" in basket)
print("x" in basket)
print("i" in "hi my name is Ian")
print(basket.count("d"))
# Exercise:
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.pop()
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)

# List Methods 2

basket = ["a", "x", "b", "c", "d", "e", "d"]
basket.sort()
print(basket)
print(sorted(basket))
new_basket = basket[:]
new_basket.sort()
print(new_basket)
basket.reverse()
print(basket)

# Common List Patterns

basket = ["a", "x", "b", "c", "d", "e", "d"]
basket.sort()
basket.reverse()
print(basket[::-1])
print(basket)
print(list(range(1, 100)))
print(list(range(100)))
sentence = " "
new_sentence = sentence.join(["hi", "my", "name", "is", "JOJO"])
print(new_sentence)
new_sentence = " ".join(["hi", "my", "name", "is", "JOJO"])
print(new_sentence)
