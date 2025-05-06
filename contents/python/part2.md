# 🧠 PYTHON GUIDE – PART 2: Intermediate to Advanced Concepts

## Table of Contents

* [User Input and Type Casting](#user-input-and-type-casting)
* [Advanced Looping Techniques](#advanced-looping-techniques)
* [Functions and Scope](#functions-and-scope)
* [Lambda, map, filter, reduce](#lambda-map-filter-reduce)
* [List, Set, and Dictionary Comprehensions](#list-set-and-dictionary-comprehensions)
* [Advanced Data Structures](#advanced-data-structures)
* [Modules and Packages](#modules-and-packages)
* [File Handling](#file-handling)
* [Sophisticated Exception Handling](#sophisticated-exception-handling)
* [Decorators](#decorators)
* [Generators](#generators)
* [Preview: Part 3](#preview-part-3)

---

## 📥 User Input and Type Casting

### `input()` – Standard Input Mechanism

The `input()` function captures data entered by the user via the console and returns it as a string object, regardless of the intended type. This behavior necessitates explicit type conversion for numerical computations or logical evaluations.

```python
name = input("Enter your name: ")
print(f"Hello, {name}")
```

### Type Casting: Explicit Conversion of Data Types

The conversion of input strings to numerical data types such as `int`, `float`, or `bool` is a foundational requirement for type safety in computation.

```python
age = int(input("Enter your age: "))
print(f"In 5 years, you'll be {age + 5}")
```

### Handling Multiple Inputs Simultaneously

Multiple scalar values can be extracted from a single input string using the `split()` method, which tokenizes the string into substrings based on a delimiter.

```python
x, y = input("Enter two numbers: ").split()
x, y = int(x), int(y)
print(x + y)
```

> 🔹 Advanced Tip: To accommodate non-space delimiters (e.g., commas or semicolons), provide an argument to `split()`, such as `split(',')`.

---

## ➡️ Advanced Looping Techniques

### `enumerate()` – Index-Aware Iteration

The `enumerate()` function yields pairs of indices and values, enabling concurrent access to element position and content.

```python
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"{index}: {name}")
```

### `zip()` – Parallel Iteration Over Multiple Sequences

Combines multiple iterable sequences into a singular iterable of tuples, facilitating synchronized iteration.

```python
names = ["Alice", "Bob"]
scores = [85, 92]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")
```

---

## 🔍 Functions and Scope

### Defining Functions

Functions are first-class citizens in Python, encapsulating reusable logic under a symbolic identifier.

```python
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))
```

### Scope and Variable Visibility

* **Global Scope**: Defined at the module level, accessible throughout.
* **Local Scope**: Defined within functions, inaccessible from the outside.

```python
x = 10

def change():
    x = 20
    print("Inside function:", x)

change()
print("Outside function:", x)
```

---

## 🧱 Lambda, map, filter, reduce

### Lambda Expressions: Anonymous Functions

Lambda expressions enable concise definition of ephemeral functions without the `def` keyword.

```python
square = lambda x: x * x
print(square(5))
```

### `map()`: Functional Mapping

Applies a function to each item of an iterable and returns a map object.

```python
nums = [1, 2, 3]
squares = list(map(lambda x: x*x, nums))
```

### `filter()`: Conditional Selection

Selects elements that satisfy a predicate function.

```python
evens = list(filter(lambda x: x % 2 == 0, nums))
```

### `reduce()`: Aggregation by Rolling Computation

Requires import from `functools`. Sequentially applies a binary function to the iterable to reduce it to a single value.

```python
from functools import reduce
product = reduce(lambda x, y: x * y, nums)
```

---

## 📊 Comprehensions for List, Set, and Dictionary

### List Comprehension

Compact syntax for generating lists.

```python
evens = [x for x in range(10) if x % 2 == 0]
```

### Set Comprehension

Generates a set of unique elements.

```python
squares = {x*x for x in range(5)}
```

### Dictionary Comprehension

Constructs key-value mappings.

```python
squares = {x: x*x for x in range(5)}
```

---

## 📂 Advanced Data Structures

### Tuples: Immutable Ordered Collections

Useful for storing heterogeneous fixed data.

```python
point = (3, 4)
```

### `namedtuple`: Semantically Rich Tuples

Enhances tuple readability by assigning named fields.

```python
from collections import namedtuple
Point = namedtuple("Point", "x y")
p = Point(1, 2)
print(p.x, p.y)
```

### `defaultdict`: Enhanced Dictionary with Default Initialization

Automatically initializes dictionary keys with a default type.

```python
from collections import defaultdict
count = defaultdict(int)
count["a"] += 1
```

---

## 📖 Modules and Packages

### Importing Predefined Modules

Standard library modules provide extensive functionality.

```python
import math
print(math.sqrt(16))
```

### Custom Module Creation

Define functions in a separate `.py` file and import them.

**mymodule.py:**

```python
def add(a, b):
    return a + b
```

**main.py:**

```python
from mymodule import add
print(add(2, 3))
```

---

## 📃 File Handling

### Reading from Files

Context manager ensures proper resource deallocation.

```python
with open("data.txt", "r") as file:
    print(file.read())
```

### Writing to Files

Overwrites or creates new content.

```python
with open("data.txt", "w") as file:
    file.write("Hello")
```

---

## 🪧 Sophisticated Exception Handling

### Use of `else` and `finally`

* `else`: Executes if no exceptions were raised.
* `finally`: Executes unconditionally.

```python
try:
    val = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("No errors occurred")
finally:
    print("This always runs")
```

---

## 🌟 Decorators

A decorator is a higher-order function that modifies the behavior of another function without permanently altering its structure.

```python
def decorator(func):
    def wrapper():
        print("Before call")
        func()
        print("After call")
    return wrapper

@decorator
def greet():
    print("Hello")

greet()
```

---

## 🔁 Generators

Generators are special iterators that yield values lazily, providing a memory-efficient mechanism for producing sequences.

```python
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

for number in count_up_to(5):
    print(number)
```

---

## ✨ Preview: Part 3

In the upcoming section, we will explore:

* Object-Oriented Programming (OOP)
* Class Hierarchies and Inheritance
* File System Navigation and JSON Processing
* Web APIs and HTTP Requests
* GUI Development via Tkinter or PyQt
* Unit Testing and Quality Assurance
