# Python Complete Notes

Date: 2026-07-09

These notes explain Python from absolute beginner level to advanced practical usage. They are designed as a foundation for machine learning, data science, automation, web apps, scripting, and general programming.

Official references checked:

- Python tutorial: https://docs.python.org/3/tutorial/
- Python standard library: https://docs.python.org/3/library/
- NumPy beginner guide: https://numpy.org/doc/stable/user/absolute_beginners.html
- pandas user guide: https://pandas.pydata.org/docs/user_guide/index.html

---

## 1. What Is Programming?

Programming means giving step-by-step instructions to a computer.

Example human instruction:

```text
Take two numbers.
Add them.
Show the result.
```

Python version:

```python
a = 10
b = 20
print(a + b)
```

Line by line:

- `a = 10`: store number `10` in variable `a`.
- `b = 20`: store number `20` in variable `b`.
- `print(a + b)`: add both values and display the result.

---

## 2. What Is Python?

Python is a high-level programming language.

It is popular because:

- syntax is simple
- huge ecosystem
- works for automation, data science, machine learning, web development, APIs, scripting, testing, and more
- large community
- many libraries

Python is interpreted, which means you usually run code directly using the Python interpreter.

---

## 3. Installing and Running Python

### 3.1 Check Version

```bash
python --version
```

or:

```bash
python3 --version
```

### 3.2 Run Python File

Create file:

```text
hello.py
```

Code:

```python
print("Hello, Python")
```

Run:

```bash
python hello.py
```

### 3.3 REPL

Run:

```bash
python
```

This opens interactive Python.

Good for quick experiments:

```python
>>> 2 + 3
5
```

---

## 4. Comments

Comments explain code for humans. Python ignores them.

```python
# This is a single-line comment
print("Hello")
```

Use comments to explain why, not obvious what.

Bad:

```python
# Add 1 to x
x = x + 1
```

Better:

```python
# Count this failed attempt before retrying.
x = x + 1
```

---

## 5. Print Statement

```python
print("Hello")
print("Python", "is", "fun")
```

Output:

```text
Hello
Python is fun
```

### 5.1 Separator

```python
print("2026", "07", "09", sep="-")
```

Output:

```text
2026-07-09
```

### 5.2 End

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

---

## 6. Escape Sequences

Escape sequences represent special characters.

```python
print("Hello\nWorld")
print("Name:\tPython")
print("She said \"Hi\"")
```

Meaning:

- `\n`: new line
- `\t`: tab
- `\"`: quote inside string

Raw string:

```python
path = r"C:\Users\Name\Documents"
print(path)
```

Raw strings reduce escaping problems with Windows paths.

---

## 7. Variables

A variable is a name for a value.

```python
name = "Asha"
age = 21
height = 1.65
is_student = True
```

Line by line:

- `name`: string variable.
- `age`: integer variable.
- `height`: float variable.
- `is_student`: boolean variable.

### 7.1 Naming Rules

Valid:

```python
user_name = "Ravi"
age2 = 20
_secret = "hidden"
```

Invalid:

```python
2age = 20
user-name = "Ravi"
class = "A"
```

Why invalid:

- variable cannot start with number
- hyphen means subtraction
- `class` is reserved keyword

### 7.2 Naming Style

Use snake_case:

```python
total_price = 500
student_marks = 95
```

---

## 8. Data Types

Common types:

| Type | Example |
|---|---|
| `int` | `10` |
| `float` | `10.5` |
| `str` | `"hello"` |
| `bool` | `True`, `False` |
| `list` | `[1, 2, 3]` |
| `tuple` | `(1, 2, 3)` |
| `set` | `{1, 2, 3}` |
| `dict` | `{"name": "Asha"}` |
| `NoneType` | `None` |

Check type:

```python
x = 10
print(type(x))
```

---

## 9. Type Casting

Type casting converts one type to another.

```python
age_text = "21"
age = int(age_text)
print(age + 1)
```

Line by line:

- `age_text` is string.
- `int(age_text)` converts string to integer.
- now arithmetic works.

More examples:

```python
print(str(100))
print(float("3.14"))
print(bool(1))
print(bool(0))
```

Important:

```python
int("hello")
```

This causes error because `"hello"` is not a valid integer.

---

## 10. User Input

```python
name = input("Enter your name: ")
print("Hello", name)
```

`input()` always returns a string.

For numbers:

```python
age = int(input("Enter your age: "))
print(age + 1)
```

Line by line:

- ask user for age
- convert text to integer
- add 1

---

## 11. Operators

### 11.1 Arithmetic Operators

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

Meaning:

- `+`: addition
- `-`: subtraction
- `*`: multiplication
- `/`: true division
- `//`: floor division
- `%`: remainder
- `**`: power

### 11.2 Comparison Operators

```python
print(10 == 10)
print(10 != 5)
print(10 > 5)
print(10 >= 10)
print(3 < 5)
print(3 <= 3)
```

These return `True` or `False`.

### 11.3 Logical Operators

```python
age = 20
has_id = True

print(age >= 18 and has_id)
print(age < 18 or has_id)
print(not has_id)
```

Meaning:

- `and`: both conditions must be true
- `or`: at least one condition must be true
- `not`: reverse boolean

---

## 12. Strings

String is text.

```python
name = "Python"
message = 'Hello'
multiline = """This is
multiple lines"""
```

### 12.1 Indexing

```python
text = "Python"

print(text[0])
print(text[1])
print(text[-1])
```

Output:

```text
P
y
n
```

Python indexing starts at 0.

### 12.2 Slicing

```python
text = "Python"

print(text[0:2])
print(text[:4])
print(text[2:])
print(text[::-1])
```

Meaning:

- `text[0:2]`: characters from index 0 up to before 2.
- `text[:4]`: beginning to before 4.
- `text[2:]`: from index 2 to end.
- `text[::-1]`: reverse string.

### 12.3 String Methods

```python
text = "  Python Programming  "

print(text.lower())
print(text.upper())
print(text.strip())
print(text.replace("Python", "Java"))
print(text.split())
print("Python" in text)
```

Common methods:

- `lower`: lowercase
- `upper`: uppercase
- `strip`: remove surrounding whitespace
- `replace`: replace substring
- `split`: split into list
- `in`: membership test

### 12.4 f-Strings

```python
name = "Asha"
score = 95

print(f"{name} scored {score} marks")
```

f-strings are the recommended way to format many strings.

---

## 13. Conditional Statements

```python
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Line by line:

- check condition
- if true, run first block
- otherwise, run else block

### 13.1 if-elif-else

```python
marks = 82

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"

print(grade)
```

Python checks from top to bottom.

### 13.2 Ternary Expression

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)
```

Use for simple conditional values.

---

## 14. Match Case

`match` is structural pattern matching.

```python
command = "start"

match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case _:
        print("Unknown command")
```

Meaning:

- compare `command` against patterns
- `_` means default case

---

## 15. Loops

### 15.1 for Loop

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

### 15.2 Loop Through List

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```

### 15.3 while Loop

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

Use `while` when you do not know exact number of repetitions.

### 15.4 break and continue

```python
for number in range(10):
    if number == 5:
        break
    print(number)
```

`break` stops loop.

```python
for number in range(5):
    if number == 2:
        continue
    print(number)
```

`continue` skips current iteration.

### 15.5 enumerate

```python
names = ["Asha", "Ravi", "Meera"]

for index, name in enumerate(names):
    print(index, name)
```

Use when you need index and value.

### 15.6 zip

```python
names = ["Asha", "Ravi"]
scores = [95, 88]

for name, score in zip(names, scores):
    print(name, score)
```

Use when looping over multiple lists together.

---

## 16. Lists

List is ordered and mutable.

```python
numbers = [10, 20, 30]
```

### 16.1 Access and Modify

```python
numbers = [10, 20, 30]

print(numbers[0])
numbers[1] = 25
print(numbers)
```

### 16.2 List Methods

```python
numbers = [3, 1, 2]

numbers.append(4)
numbers.remove(1)
numbers.sort()

print(numbers)
```

Common methods:

- `append`: add item at end
- `remove`: remove first matching item
- `pop`: remove by index
- `sort`: sort in place
- `reverse`: reverse in place

### 16.3 List Comprehension

```python
squares = [x ** 2 for x in range(5)]
print(squares)
```

With condition:

```python
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)
```

---

## 17. Tuples

Tuple is ordered and immutable.

```python
point = (10, 20)
print(point[0])
```

Use tuples for fixed collections.

Tuple unpacking:

```python
x, y = point
print(x, y)
```

---

## 18. Sets

Set is unordered and stores unique values.

```python
numbers = {1, 2, 2, 3}
print(numbers)
```

Output contains unique values.

Set operations:

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a & b)
print(a - b)
```

Meaning:

- `|`: union
- `&`: intersection
- `-`: difference

---

## 19. Dictionaries

Dictionary stores key-value pairs.

```python
student = {
    "name": "Asha",
    "age": 21,
    "marks": 95
}

print(student["name"])
```

### 19.1 Safe Access

```python
print(student.get("city", "Unknown"))
```

If key is missing, return default value.

### 19.2 Add and Update

```python
student["city"] = "Bengaluru"
student["marks"] = 98
```

### 19.3 Loop Through Dictionary

```python
for key, value in student.items():
    print(key, value)
```

---

## 20. Functions

Function is reusable code.

```python
def greet(name):
    return f"Hello, {name}"

message = greet("Asha")
print(message)
```

Line by line:

- `def greet(name)`: define function with parameter `name`.
- `return`: send result back.
- `greet("Asha")`: call function.

### 20.1 Default Arguments

```python
def greet(name="friend"):
    return f"Hello, {name}"

print(greet())
print(greet("Ravi"))
```

### 20.2 Keyword Arguments

```python
def describe_person(name, age):
    print(f"{name} is {age} years old")

describe_person(age=21, name="Asha")
```

### 20.3 *args

```python
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3, 4))
```

`*numbers` collects many positional arguments into a tuple.

### 20.4 **kwargs

```python
def print_profile(**details):
    for key, value in details.items():
        print(key, value)

print_profile(name="Asha", age=21, city="Bengaluru")
```

`**details` collects keyword arguments into a dictionary.

### 20.5 Lambda

```python
square = lambda x: x ** 2
print(square(5))
```

Use lambdas for short anonymous functions. Do not overuse them.

---

## 21. Scope

Scope decides where a variable can be used.

```python
x = 10

def show():
    y = 20
    print(x)
    print(y)

show()
print(x)
```

`x` is global.

`y` is local to function.

---

## 22. Modules

A module is a Python file you can import.

`math_utils.py`:

```python
def add(a, b):
    return a + b
```

`main.py`:

```python
from math_utils import add

print(add(2, 3))
```

### 22.1 Built-In Modules

```python
import math
import random
import datetime

print(math.sqrt(16))
print(random.randint(1, 10))
print(datetime.datetime.now())
```

---

## 23. pip and Virtual Environments

### 23.1 Why Virtual Environments?

Different projects need different package versions.

Virtual environment keeps dependencies separate.

Create:

```bash
python -m venv .venv
```

Activate Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Activate macOS/Linux:

```bash
source .venv/bin/activate
```

Install package:

```bash
pip install pandas
```

Save dependencies:

```bash
pip freeze > requirements.txt
```

Install from file:

```bash
pip install -r requirements.txt
```

---

## 24. File Handling

### 24.1 Read File

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

Line by line:

- `open`: open file.
- `"r"`: read mode.
- `encoding="utf-8"`: text encoding.
- `with`: closes file automatically.
- `file.read()`: read entire file.

### 24.2 Write File

```python
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello file")
```

`"w"` overwrites existing file.

Append:

```python
with open("output.txt", "a", encoding="utf-8") as file:
    file.write("\nAnother line")
```

### 24.3 Read Lines

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

---

## 25. JSON

JSON is common for APIs and configuration.

```python
import json

person = {"name": "Asha", "age": 21}

json_text = json.dumps(person)
print(json_text)

back_to_dict = json.loads(json_text)
print(back_to_dict["name"])
```

Save JSON file:

```python
with open("person.json", "w", encoding="utf-8") as file:
    json.dump(person, file, indent=2)
```

Read JSON file:

```python
with open("person.json", "r", encoding="utf-8") as file:
    data = json.load(file)
```

---

## 26. Exceptions

Errors happen. Exceptions let you handle them.

```python
try:
    number = int(input("Enter number: "))
    print(10 / number)
except ValueError:
    print("Please enter a valid integer")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Success")
finally:
    print("Done")
```

Meaning:

- `try`: code that may fail.
- `except`: handle specific error.
- `else`: run if no error.
- `finally`: always run.

Raise your own error:

```python
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```

---

## 27. Object-Oriented Programming

### 27.1 Class and Object

Class is a blueprint.

Object is an instance.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def passed(self):
        return self.marks >= 40

student = Student("Asha", 95)
print(student.name)
print(student.passed())
```

Line by line:

- `class Student`: define class.
- `__init__`: constructor, runs when object is created.
- `self.name`: store data on object.
- `passed`: method.
- `Student("Asha", 95)`: create object.

### 27.2 Instance vs Class Variables

```python
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name
```

- `school`: class variable shared by all objects.
- `name`: instance variable unique per object.

### 27.3 Inheritance

```python
class Animal:
    def speak(self):
        return "sound"

class Dog(Animal):
    def speak(self):
        return "bark"

dog = Dog()
print(dog.speak())
```

Inheritance lets a class reuse and customize another class.

### 27.4 Encapsulation

Encapsulation means keeping data and behavior together and controlling access.

Python uses convention:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount

    def get_balance(self):
        return self._balance
```

Single underscore means internal use by convention.

### 27.5 Dataclasses

```python
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float

product = Product("Book", 250.0)
print(product)
```

Dataclasses reduce boilerplate for simple data objects.

---

## 28. Iterators and Generators

### 28.1 Iterator

An iterator gives values one at a time.

```python
numbers = iter([1, 2, 3])

print(next(numbers))
print(next(numbers))
print(next(numbers))
```

### 28.2 Generator

Generator creates values lazily.

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for number in count_up_to(3):
    print(number)
```

`yield` pauses function and returns a value.

Useful for large data streams.

---

## 29. Decorators

Decorator wraps a function.

```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def greet(name):
    return f"Hello {name}"

print(greet("Asha"))
```

Line by line:

- `log_call` accepts a function.
- `wrapper` adds behavior.
- `return func(...)`: calls original function.
- `@log_call`: applies decorator.

Common uses:

- logging
- timing
- authentication
- caching

---

## 30. Context Managers

Context managers manage setup and cleanup.

```python
with open("file.txt", "w", encoding="utf-8") as file:
    file.write("hello")
```

File closes automatically.

Custom context manager:

```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("setup")
    try:
        yield
    finally:
        print("cleanup")

with managed_resource():
    print("using resource")
```

---

## 31. Type Hints

Type hints document expected types.

```python
def add(a: int, b: int) -> int:
    return a + b
```

They do not enforce types at runtime by default, but help:

- editors
- linters
- documentation
- maintainability

### 31.1 Common Type Hints

```python
from typing import Optional

def greet(name: str | None) -> str:
    if name is None:
        return "Hello"
    return f"Hello {name}"
```

`str | None` means value can be string or None.

---

## 32. Testing

Testing checks code works.

`calculator.py`:

```python
def add(a, b):
    return a + b
```

`test_calculator.py`:

```python
from calculator import add

def test_add():
    assert add(2, 3) == 5
```

Run:

```bash
pytest
```

Why tests matter:

- catch bugs early
- make refactoring safer
- document expected behavior

---

## 33. Debugging

### 33.1 Print Debugging

```python
x = 10
print("x =", x)
```

### 33.2 Breakpoint

```python
def calculate(a, b):
    breakpoint()
    return a + b

calculate(2, 3)
```

When Python reaches `breakpoint()`, debugger opens.

Useful commands:

- `n`: next line
- `s`: step into function
- `c`: continue
- `p variable`: print variable
- `q`: quit

---

## 34. Logging

Use logging instead of print in real applications.

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program started")
logging.warning("This is a warning")
logging.error("Something failed")
```

Logging supports:

- severity levels
- timestamps
- file output
- structured logs

---

## 35. Working With Dates and Times

```python
from datetime import datetime, timedelta

now = datetime.now()
tomorrow = now + timedelta(days=1)

print(now)
print(tomorrow)
```

Format:

```python
print(now.strftime("%Y-%m-%d"))
```

Parse:

```python
date = datetime.strptime("2026-07-09", "%Y-%m-%d")
```

---

## 36. Regular Expressions

Regex finds patterns in text.

```python
import re

text = "Email me at user@example.com"
match = re.search(r"[\w.-]+@[\w.-]+", text)

if match:
    print(match.group())
```

Useful for:

- validation
- extraction
- cleaning text

Do not use regex for everything. If a proper parser exists, use it.

---

## 37. Command-Line Arguments

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", required=True)
parser.add_argument("--age", type=int, default=18)

args = parser.parse_args()

print(f"{args.name} is {args.age}")
```

Run:

```bash
python app.py --name Asha --age 21
```

---

## 38. pathlib

`pathlib` is modern path handling.

```python
from pathlib import Path

path = Path("data") / "file.txt"

if path.exists():
    print(path.read_text(encoding="utf-8"))
else:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("hello", encoding="utf-8")
```

Benefits:

- readable
- cross-platform
- object-oriented

---

## 39. CSV Files

```python
import csv

rows = [
    {"name": "Asha", "score": 95},
    {"name": "Ravi", "score": 88}
]

with open("scores.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(rows)
```

Read:

```python
with open("scores.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["score"])
```

For data science, pandas is usually more convenient.

---

## 40. NumPy Basics

NumPy is used for numerical arrays.

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)
print(a * b)
print(a.mean())
```

Line by line:

- import NumPy as `np`.
- create arrays.
- operations are vectorized.
- `mean` calculates average.

### 40.1 Array Shape

```python
x = np.array([[1, 2, 3], [4, 5, 6]])

print(x.shape)
print(x.ndim)
print(x.dtype)
```

### 40.2 Reshape

```python
x = np.arange(12)
y = x.reshape(3, 4)
print(y)
```

Shape must keep same number of elements.

### 40.3 Boolean Masking

```python
x = np.array([1, 2, 3, 4, 5])
print(x[x > 3])
```

Output:

```text
[4 5]
```

---

## 41. pandas Basics

pandas is used for tabular data.

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Asha", "Ravi", "Meera"],
    "score": [95, 88, 92]
})

print(df)
print(df.head())
print(df.info())
print(df.describe())
```

### 41.1 Select Columns

```python
print(df["name"])
print(df[["name", "score"]])
```

### 41.2 Filter Rows

```python
high_scores = df[df["score"] >= 90]
print(high_scores)
```

### 41.3 Add Column

```python
df["passed"] = df["score"] >= 40
```

### 41.4 Missing Values

```python
print(df.isna().sum())
df = df.dropna()
```

Or:

```python
df["score"] = df["score"].fillna(df["score"].mean())
```

---

## 42. Async Python

Async helps with many waiting tasks, such as network calls.

```python
import asyncio

async def say_hello():
    await asyncio.sleep(1)
    print("Hello")

async def main():
    await say_hello()

asyncio.run(main())
```

Meaning:

- `async def`: define async function.
- `await`: wait without blocking event loop.
- `asyncio.run`: run async program.

Async is not magic speed for CPU-heavy work. It helps I/O-heavy work.

---

## 43. Concurrency Basics

Python has:

- threading
- multiprocessing
- asyncio

Use threading for I/O-bound tasks:

```python
from concurrent.futures import ThreadPoolExecutor

def fetch(id):
    return f"result {id}"

with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(fetch, range(10)))

print(results)
```

Use multiprocessing for CPU-bound tasks:

```python
from concurrent.futures import ProcessPoolExecutor

def square(x):
    return x * x

with ProcessPoolExecutor() as executor:
    results = list(executor.map(square, range(10)))
```

---

## 44. Project Structure

Recommended:

```text
my_project/
  src/
    my_project/
      __init__.py
      core.py
  tests/
    test_core.py
  README.md
  pyproject.toml
  requirements.txt
```

Why:

- code is organized
- tests are separate
- dependencies are documented
- project is easier to maintain

---

## 45. Clean Code Habits

Good habits:

- use clear variable names
- keep functions small
- avoid repeated code
- handle errors intentionally
- write tests for important logic
- use virtual environments
- format code
- lint code
- document important decisions

Tools:

- `ruff`: linting and formatting
- `black`: formatting
- `pytest`: testing
- `mypy` or `pyright`: type checking

---

## 46. Practice Projects

### 46.1 Beginner

- calculator
- unit converter
- number guessing game
- simple password generator
- contact book
- quiz app

### 46.2 Intermediate

- expense tracker with CSV
- weather API app
- web scraper
- file organizer
- command-line todo app
- Flask/FastAPI API

### 46.3 Data and ML Preparation

- analyze CSV with pandas
- clean missing values
- visualize sales data
- build simple regression model
- build classification model
- create dashboard

---

## 47. Python Cheat Sheet

Variables:

```python
name = "Asha"
age = 21
```

Condition:

```python
if age >= 18:
    print("adult")
```

Loop:

```python
for item in items:
    print(item)
```

Function:

```python
def add(a, b):
    return a + b
```

List:

```python
items = [1, 2, 3]
items.append(4)
```

Dictionary:

```python
person = {"name": "Asha"}
print(person["name"])
```

File:

```python
with open("file.txt", "r", encoding="utf-8") as file:
    text = file.read()
```

Class:

```python
class Person:
    def __init__(self, name):
        self.name = name
```

---

## 48. Final Python Mental Model

Python programs are built from:

```text
values -> variables -> expressions -> statements -> functions -> modules -> packages -> applications
```

To solve any Python problem:

1. Understand the input.
2. Understand the expected output.
3. Break the task into small steps.
4. Write one function at a time.
5. Test with simple examples.
6. Handle edge cases.
7. Refactor for clarity.

Python becomes powerful when you combine simple basics with good problem-solving habits.

