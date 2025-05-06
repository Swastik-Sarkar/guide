# 📘 INTRODUCTION TO PYTHON 

Python is a high-level, general-purpose programming language renowned for its clear syntax and readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming, making it ideal for both beginner and advanced-level software development.

## 🛠️ Prerequisites

* Python 3.x ([Install Python](https://www.python.org/downloads/))
* A code editor or IDE (e.g., VS Code, PyCharm, or Sublime Text)

## 🧭 Contents

* [Basic Syntax](#basic-syntax)
* [Statements](#statements)
* [Data Types](#data-types)
* [Mathematical Operators](#mathematical-operators)
* [Exception Handling](#exception-handling)
* [Assertions](#assertions)
* [String Literals](#string-literals)
* [Text Manipulation](#text-manipulation)
* [(Goto Next Part ➡)](#goto-next-part)

---

## 🔤 Basic Syntax

```python
print("Hello, World!")
```

Python emphasizes simplicity and readability. The `print()` function outputs data to the console. Unlike languages like Java or C++, no boilerplate code is required to begin writing meaningful programs.

---

## 🧾 Statements

### 📥 I/O Statements

* `print()` — Displays output to the console.
* `input()` — Reads a line of input from the user.

### 🔍 Conditional Statements

```python
if condition:
    # block of code
elif another_condition:
    # block of code
else:
    # block of code
```

Example:

```python
if 2 + 2 == 4:
    print("Correct")
elif 2 + 2 == 3:
    print("Incorrect")
else:
    print("Impossible")
```

### 🔁 Looping Constructs

#### While Loop

```python
while condition:
    # block of code
```

Example:

```python
counter = 0
while counter < 3:
    print("Counting", counter)
    counter += 1
```

#### Infinite Loop (Use with Caution)

```python
while True:
    print("Looping forever")
    break  # use break to exit
```

### 🧯 Exception Handling

```python
try:
    # code that may raise an exception
except ExceptionType:
    # handling code
```

Example:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### 🔁 Control Statements

```python
for i in range(5):
    if i == 2:
        continue  # skips iteration
    if i == 4:
        break  # exits loop
    print(i)
```

### 🔂 pass Statement

Acts as a placeholder for future code.

```python
if True:
    pass
```

---

## 📚 Data Types

Python supports a wide range of data types:

### 🔢 Numeric

* `int`: Whole numbers (e.g., 5)
* `float`: Decimal numbers (e.g., 3.14)
* `complex`: Numbers with real and imaginary parts (e.g., 4 + 3j)

### 🔠 Sequence

* `str`: Text (e.g., "Hello")
* `list`: Ordered and mutable (e.g., \[1, 2, 3])
* `tuple`: Ordered and immutable (e.g., (1, 2, 3))

### 🔑 Mapping

* `dict`: Key-value pairs (e.g., {"name": "Alice"})

### 🔘 Set

* `set`: Unordered, unique values (e.g., {1, 2, 3})
* `frozenset`: Immutable version of set

### 🟢 Boolean

* `bool`: Represents `True` or `False`

### 🧬 Binary (**Advanced**)

* `bytes`, `bytearray`, `memoryview`

### ⚪ None Type

* `None`: Represents absence of value

---

## ➕ Mathematical Operators

Python provides a full suite of arithmetic operators:

* `+` Addition
* `-` Subtraction
* `*` Multiplication
* `/` Division (float result)
* `//` Floor Division
* `%` Modulo (remainder)
* `**` Exponentiation

---

## ⚠️ Exception Handling

Understanding exceptions helps you write robust, crash-free programs.

Common Python exceptions:

* `SyntaxError`
* `TypeError`
* `NameError`
* `IndexError`
* `KeyError`
* `ValueError`
* `AttributeError`
* `IOError`
* `ZeroDivisionError`
* `ImportError`
* `AssertionError`
* `IndentationError`
* `NotImplementedError`
* `StopIteration`
* `FloatingPointError`
* `LookupError`

---

## ✅ Assertions

Assertions are used for debugging and enforcing conditions.

```python
x = 5
assert x > 10, "x must be greater than 10"
```

If the condition is false, an `AssertionError` is raised.

---

## 🧵 String Literals

Types of strings in Python:

1. **Multi-line Strings**:

```python
print("""Line 1
Line 2
Line 3""")
```

2. **Raw Strings** (ignores escape sequences):

```python
print(r"C:\Users\Admin")
```

3. **Formatted Strings** (f-strings):

```python
a = 42
print(f"The answer is {a}")
```

---

## 📝 Text Manipulation

Common string operations:

```python
s = "Hello World"
print(s.upper())     # HELLO WORLD
print(s.lower())     # hello world
```

### Converting and Concatenating

```python
a = 5
b = 10
print("Value:", a)
print("Sum: " + str(a + b))
```

---

#### 🔗 [Goto Next Part ➡](https://github.com/Swastik-Sarkar/guides/blob/main/contents/python/part2.md)
