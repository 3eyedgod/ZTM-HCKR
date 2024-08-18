"""
Ultimate Python Cheat Sheet

This script provides a comprehensive overview of Python basics and advanced topics,
including data types, control flow, functions, error handling, file I/O, OOP,
concurrency, and more. Each section is commented to explain the process in detail.

For more detailed explanations, refer to the official Python documentation:
https://docs.python.org/3/
"""

# Table of Contents
"""
1. Basic Syntax and Operations
    - Operator Precedence
2. Data Types
    - Integer, Float, Complex, String, List, Tuple, Set, Dictionary
3. Variables and Constants
4. Control Flow
    - Conditional Statements, Loops
5. Functions and Modules
6. Error Handling
7. File I/O
8. Object-Oriented Programming (OOP)
9. Libraries and Packages
10. Advanced Data Structures
11. Concurrency and Parallelism
"""

# 1. Basic Syntax and Operations
"""
Python uses operator precedence to determine the order of operations in an expression.
This follows the PEMDAS rule: Parentheses, Exponents, Multiplication and Division,
Addition and Subtraction. Understanding operator precedence is essential for writing
correct expressions.

Refer to the documentation for more details:
https://docs.python.org/3/reference/expressions.html#operator-precedence
"""

# Operator Precedence Examples
print((3 + 2) * 5)  # (3 + 2) is evaluated first to 5, then 5 * 5 = 25
print(2**3)  # Exponentiation: 2^3 = 8
print(
    4 * 3 / 2
)  # Multiplication and division are left-associative: 4 * 3 = 12, 12 / 2 = 6.0
print(
    10 + 5 - 3
)  # Addition and subtraction are left-associative: 10 + 5 = 15, 15 - 3 = 12
print(
    10 + 2 * 3**2
)  # Exponentiation first: 3 ** 2 = 9, then multiplication: 2 * 9 = 18, finally addition: 10 + 18 = 28

# 2. Data Types
"""
Python supports several built-in data types: int, float, complex, str, list, tuple, set, and dict.

Learn more about Python's data types:
https://docs.python.org/3/library/stdtypes.html
"""

# Integer
age = 25  # Integer type
print(age)

# Float
height = 5.9  # Float type for decimal numbers
print(height)

# Complex Number
complex_num = 3 + 4j  # Complex numbers have a real and imaginary part
print(complex_num)
print(complex_num.real)  # Accessing the real part
print(complex_num.imag)  # Accessing the imaginary part

# String
text = "Hello, World!"  # Strings are sequences of characters
print(text)

# List
numbers = [1, 2, 3, 4, 5]  # Lists are ordered, mutable sequences
print(numbers)

# Tuple
coordinates = (10.0, 20.0)  # Tuples are ordered, immutable sequences
print(coordinates)

# Set
unique_numbers = {1, 2, 3, 2, 1}  # Sets are unordered collections of unique elements
print(unique_numbers)

# Dictionary
student = {
    "name": "John",
    "age": 20,
    "major": "Computer Science",
}  # Dictionaries store key-value pairs
print(student)

# 3. Variables and Constants
"""
Variables are used to store data that can be modified. Constants are values that do not change.

More on Python variables:
https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator
"""

# Variable Assignment
name = "Alice"
print(name)

# Variable Reassignment
age = 30
print(age)
age = 31
print(age)

# Constants
PI = 3.14159  # Constants are typically written in uppercase
print(PI)

# 4. Control Flow
"""
Control flow includes conditional statements and loops, which allow for decision-making
and repetition in your code.

Read more on control flow:
https://docs.python.org/3/tutorial/controlflow.html
"""

# Conditional Statements
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# Loops

# For Loop
for i in range(5):
    print(i)  # Iterates from 0 to 4

# While Loop
i = 0
while i < 5:
    print(i)  # Iterates while i < 5
    i += 1  # Increments i by 1 each iteration

# 5. Functions and Modules
"""
Functions are blocks of code that perform specific tasks. Modules are files containing Python code
that can be imported into other Python scripts.

Explore more about functions and modules:
- Functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- Modules: https://docs.python.org/3/tutorial/modules.html
"""


# Function Definition
def greet(name):
    """
    Function to greet a person by name.

    Args:
        name (str): The name of the person.

    Returns:
        str: Greeting message.
    """
    return f"Hello, {name}!"


print(greet("Alice"))


# Function with Default Arguments
def add(a, b=5):
    """
    Adds two numbers, with a default value for the second number.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 5.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b


print(add(3))  # Uses default value for b
print(add(3, 4))  # Overrides default value for b

# Importing Modules
import math

print(math.sqrt(16))  # Uses the math module to compute the square root of 16

# 6. Error Handling
"""
Error handling in Python is done using try, except, finally, and raise keywords to manage exceptions
and ensure proper execution of code.

Learn more about error handling:
https://docs.python.org/3/tutorial/errors.html
"""

# Try-Except Block
try:
    result = 10 / 0  # This will cause a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")  # Catches the exception and prints an error message

# Finally Block
try:
    file = open("example.txt", "r")  # Attempts to open a file for reading
finally:
    file.close()  # Ensures the file is closed after the operation, even if an error occurs


# Raising Exceptions
def divide(x, y):
    """
    Divides two numbers and raises an exception if the divisor is zero.

    Args:
        x (int or float): The numerator.
        y (int or float): The denominator.

    Raises:
        ValueError: If y is zero.

    Returns:
        int or float: The result of division.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y


print(divide(10, 2))  # Outputs 5.0
# Uncomment the next line to see the exception raised
# print(divide(10, 0))

# 7. File I/O
"""
Reading from and writing to files is essential for persistent data storage.

More on file I/O:
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Writing to a File
with open("output.txt", "w") as file:
    file.write("Hello, World!")  # Writes "Hello, World!" to the file

# Reading from a File
with open("output.txt", "r") as file:
    content = file.read()  # Reads the content of the file
    print(content)  # Outputs the content: "Hello, World!"

# 8. Object-Oriented Programming (OOP)
"""
OOP is a programming paradigm based on the concept of objects. Python supports classes and inheritance.

More on OOP in Python:
https://docs.python.org/3/tutorial/classes.html
"""


# Class Definition
class Person:
    """
    Represents a person.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
    """

    def __init__(self, name, age):
        self.name = name  # Initializes the name attribute
        self.age = age  # Initializes the age attribute

    def greet(self):
        """
        Greets the person with their name and age.

        Returns:
            str: Greeting message.
        """
        return f"Hi, my name is {self.name} and I am {self.age} years old."


person = Person("Alice", 30)
print(person.greet())  # Outputs the greeting message


# Inheritance
class Student(Person):
    """
    Represents a student, which is a subclass of Person.

    Attributes:
        student_id (str): The student ID.
    """

    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Calls the constructor of the base class
        self.student_id = student_id  # Initializes the student_id attribute

    def greet(self):
        """
        Greets the student with their name and student ID.

        Returns:
            str: Greeting message with student ID.
        """
        return f"Hi, I am {self.name}, a student with ID {self.student_id}."


student = Student("Bob", 22, "S12345")
print(student.greet())  # Outputs the greeting message with student ID

# 9. Libraries and Packages
"""
Python has a rich ecosystem of libraries and packages for various tasks.

For more on Python libraries:
https://docs.python.org/3/tutorial/modules.html
"""

# Using a Library
import numpy as np

array = np.array([1, 2, 3])  # Creates a numpy array
print(array)  # Outputs the numpy array: [1 2 3]

# 10. Advanced Data Structures
"""
Advanced data structures include linked lists, trees, and heaps. Python's built-in structures
are often sufficient, but custom implementations can be useful.

Learn more about data structures:
https://docs.python.org/3/tutorial/datastructures.html
"""


# Linked List Example (Simple Implementation)
class Node:
    """
    Represents a node in a linked list.

    Attributes:
        value (Any): The value stored in the node.
        next (Node or None): The next node in the list.
    """

    def __init__(self, value):
        self.value = value  # Node's value
        self.next = None  # Pointer to the next node


class LinkedList:
    """
    Represents a linked list.

    Attributes:
        head (Node or None): The head of the linked list.
    """

    def __init__(self):
        self.head = None  # Initializes the head of the linked list

    def append(self, value):
        """
        Appends a new node with the given value to the end of the list.

        Args:
            value (Any): The value to append.
        """
        new_node = Node(value)  # Creates a new node
        if not self.head:
            self.head = new_node  # If the list is empty, set head to the new node
            return
        last = self.head
        while last.next:
            last = last.next  # Traverse to the end of the list
        last.next = new_node  # Append the new node

    def display(self):
        """
        Displays the linked list.
        """
        current = self.head
        while current:
            print(current.value, end=" -> ")  # Print the node's value
            current = current.next
        print("None")  # End of list


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.display()  # Outputs: 1 -> 2 -> 3 -> None

# Heap Example (Using heapq)
import heapq

heap = []
heapq.heappush(heap, 3)  # Pushes 3 onto the heap
heapq.heappush(heap, 1)  # Pushes 1 onto the heap
heapq.heappush(heap, 2)  # Pushes 2 onto the heap

print(heapq.heappop(heap))  # Pops and prints the smallest item: 1
print(heapq.heappop(heap))  # Pops and prints the next smallest item: 2
print(heapq.heappop(heap))  # Pops and prints the last item: 3

# 11. Concurrency and Parallelism
"""
Concurrency and parallelism involve executing multiple tasks simultaneously. Python provides
threading and multiprocessing modules for this purpose.

More on concurrency and parallelism:
https://docs.python.org/3/library/concurrency.html
"""

# Threading
import threading


def print_numbers():
    """
    Prints numbers from 0 to 4 in a separate thread.
    """
    for i in range(5):
        print(i)


thread = threading.Thread(target=print_numbers)
thread.start()  # Starts the thread
thread.join()  # Waits for the thread to finish

# Multiprocessing
from multiprocessing import Process


def print_numbers():
    """
    Prints numbers from 0 to 4 in a separate process.
    """
    for i in range(5):
        print(i)


process = Process(target=print_numbers)
process.start()  # Starts the process
process.join()  # Waits for the process to finish

print("Done")  # Indicates that multiprocessing is complete

"""
For further reading and exploration, visit the Python documentation:
https://docs.python.org/3/
"""
