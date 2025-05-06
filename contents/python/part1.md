# INTRODUCTION TO PYTHON

Python is a coding laguage known for its simplicity and easy understandable syntax.

## Prerequisite

- Latest python version ([Install Python](https://www.python.org/downloads/))
- Code Editor of your choice

## Contents

- [INTRODUCTION TO PYTHON](#introduction-to-python)
  - [Prerequisite](#prerequisite)
  - [Contents](#contents)
  - [Basic Syntax](#basic-syntax)
  - [Statements](#statements)
  - [Data types](#data-types)
  - [Mathmetical Operators](#mathmetical-operators)
  - [Identifying Errors using exception](#identifying-errors-using-exception)
  - [Assertions in python](#assertions-in-python)
  - [String Literals](#string-literals)
  - [Text manipulation](#text-manipulation)
      - [(Goto Next Part?)](#goto-next-part)

---

## Basic Syntax

```python
print("Hello World!")

# = OUTPUT = #
# Hello World!
```

As we can see, python is very straight forward and easy to understand compared to other programing languages

Now let's learn about some basic statements

---

## Statements

**I/O (input/output) statements :**

- `print()` &larr; Used to print text
- `input()` &larr; Allows user to input data
  
  **Logical statements :**
- `if`, `else` & `elif` statemnt:
  - Syntax:

      ```python
          if <expression>:
            <statements>
          elif <expression>:
            <statements>
          else:
            <statements>
      ```

      For example:

      ```python
        if 2 + 2 == 4:
          print("2 + 2 is 4") 
        else if 2 + 2 == 3:
          print("2 + 2 is 3")
        else:
          print("2 + 2 is 2")
        # = OUTPUT = #
        # 2 + 2 is 4
      ```

- `while` statement:
  - Syntax:
        ```python
          while <expression>:
            <statements>
        ```
        For example:
        ```python
          while 1 + 1 == 2:
            print("yes")
        # = OUTPUT = #
        # yes
        # yes
        # yes
        # ...
        ```
        here it forms a **loop** (we will learn about that a little later), in simple terms... Since we know 1 + 1 = 2, the while statement prints *"yes"* but as there is no `break` statement or some other instruction... it will keep on printing *"yes"* infinitly until stopped by the user

**Error handling statements:**

- `try` & `except` statement:
  - Syntax:

      ```python
          try:
            <statements>
          except:
            <statements>
      ```

      for example:

      ```python
        try:
          print("This is a text!")
        except:
          print("An error occured :(")
      ```

      here the `try` statement tries to print *"This is a text!"* if some error occours...it prints *"An error occured :("* instead of crashing the program

**Control statements:**

- `break` & `continue`:
  - Syntax:
        ```python
            # With if statement as example
            if <expression>:
              break # if expression is true, program ends
            else:
              <statements>
              continue # if expression is false, continues

        ```
      for example:
        ```python
          # ( INTERMEDIATE LEVEL EXAMPLE ) #
          x = input("n = ")
          for i in range(0, x):
            if i = 1:
              continue
            print(i)
            # = OUTPUT = #
            # n = 4
            # 0
            # 2
            # 3
        ```
        Here *input("n = ")* takes input from user and value is stored in variable *x*, *range(0, x)* generates numbers starting from 0 up to x-1, *if i == 1:* checks if i is equal to 1, continue skips the printing step if i is 1, *print(i)* prints the current value of i if it's not skipped.

       `break` &larr; ends program <br> `continue` &larr; skips/continues a statement
**pass statement:**
`pass` statement is a placeholder for future code.
Syntax:

  ```python
  if <expression>:
    pass
  ```

for example:

  ```python
  print("hi")
  if 1 + 1 = 2:
    pass
  # = OUTPUT = #
  # hi
  ```

  here the if statement gets skipped
**loops:**
Loops are infinitely running peice of code made using a logical statement. Loops are generally formed when a logic is always True.
Example:

  ```python
  while True:
    print("Hello World!")
  # = OUTPUT = #
  # Hello World!
  # Hello World!
  # Hello World!
  # ...
  ```

since `True` is always True it falls into a loop
  
**PRO TIP:**
using a break statment can stop these type of loops.
Example:
(using while loop)

  ```python
      while True:
        <statements>

        break
  ```

## Data types

**Data types are generally of 7 types:**

- Numeric Types:
  - `int` &larr; Represents integers. (eg: 10, 0, -10)
  - `float` &larr; Represents floating point numbers. (eg: 3.14, 0.00001, -23.12)
  - `complex` &larr; Represents complex numbers (eg: 5 + j, 3 + 2j, 12 + j)
- Sequence Types:
  - `str` &larr; Represents strings which are sentences/sequences of characters. (eg: "hi", "hello wassup")
  - `list` &larr; Represents ordered, mutable(changable) sequences of items (eg: [1, 2, 3], ['a', 'b', 'c'])
  - `tuple` &larr; Represents ordered, immutable(unchangeable) sequence of items (eg: (1, 2, 3), ('a', 'b', 'c'))
- Mapping Types:
  - `dict` &larr; Represents dictionaries, which are collection of key value pairs. (eg: {"a": "1", "2": "b"})
- Set types:
  - `set` &larr; Represents sets, which are unordered collections of unique values. (eg: {1, 2, 3})
  - `frozenset` &larr; Represents sets but immutable.
- Boolean types:
  - `bool` &larr; Represents booleans. (eg: True, False)
- Binary types: (**!ADVANCE LEVEL!**):
  - `bytes` &larr; Represnts immutable sequences of bytes.
  - `bytearray` &larr; Represents mutable sequences of bytes.
  - `memoryview` &larr; Creates a view of the byte array, allowing direct access to memory.
- None Type:
  - `none` &larr; Represents absense of value. (eg: none)

## Mathmetical Operators

We can do simple to complex mathmetics using python!

**Some operands are:**

- `+` &larr; addition
- `-` &larr; substraction
- `/` &larr; division
- `//` &larr; floor division(no decimal point)
- `**` &larr; power
- `*` &larr; multiplication
- `%` &larr; modulus(remainder)

## Identifying Errors using exception

Identifying the errors in your program is like a cheatcode to fix it very fast

**Some error types are**

- `SyntaxError`&larr; Raised when the code contains syntax errors, like typos or incorrect grammar.
- `TypeError`&larr; Occurs when an operation or function is applied to an object of an inappropriate type.
- `NameError`&larr; Raised when a variable is not found in the local or global scope.
- `IndexError`&larr; Triggered when trying to access an index that is out of range in a sequence (like a list or tuple).
- `KeyError`&larr; Raised when trying to access a key that does not exist in a dictionary.
- `ValueError`&larr; Occurs when a function receives an argument of the correct type but an inappropriate value.
- `AttributeError`&larr; Raised when an object does not have the attribute being accessed.
- `IOError`&larr; Triggered when an input/output operation (like file reading or writing) fails.
- `ZeroDivisionError`&larr; Raised when dividing a number by zero.
- `ImportError`&larr; Occurs when an import statement fails to find or load a module.
- `AssertionError`&larr; Raised when an `assert` statement fails (the condition evaluates to false).
- `IndentationError`&larr; Raised when the indentation of the code is incorrect.
- `NotImplementedError`&larr; Occurs when an abstract method or function is not implemented in a derived class.
- `StopIteration`&larr; Signals the end of an iteration sequence, raised when an iterator has no more items.
- `FloatingPointError`&larr; Raised when a floating-point operation fails.
- `LookupError`&larr; Base class for exceptions related to lookup operations, such as `IndexError` and `KeyError`.

## Assertions in python

We can assert values and raise a `AssertionError` if the expression is False.
Example:

```python
x = 2
assert x > 10, "x should be greater than 10"
# = OUTPUT = #
# ...
# AssertionError: x should be greater than 10
```

Since we asserted that x is greater than 10... if we assign value less than 10 to x, it will raise `AssertionError`.

## String Literals

Types:

1. Multi line strings &larr; Allows user to use multiple lines.
   - usage:

     ```python
     print("""line1
     line 2
     line 3
     """)
     ```

2. Raw strings &larr; Allows users to bypass escape sequence characters and print them.
    - usage:
      `print(r"C:\Users\Admin")`

3. Formatted strings &larr; Allows user to call variables inside a string.
    - usage:

      ```python
      a = 1
      print(f"Value of A is : {a}) # {} is used to call the variable
      ```

## Text manipulation

We can manipulate text in various ways!
Usage:
  `"string".manipulator()` (except for 3.)

1. `upper()` &larr; Format's text in Uppercase
2. `lower()` &larr; Format's text in Lowercase
3. Variables with text:
   - Example:

     ```python
     a = 5
     print("string", a) # Best way to use int with str
     b = 10
     c = str(b) # Conversion Of STRING to INTEGER
     print("string" + c)
     # = OUTPUT = #
     # string 5
     # string10
     ```

#### ([Goto Next Part?](https://github.com/Swastik-Sarkar/guides/blob/main/contents/python/part2.md))
