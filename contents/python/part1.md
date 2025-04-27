# INTRODUCTION TO PYTHON

Python is a coding laguage known for its simplicity and easy understandable syntax.

## Prerequisite
- Latest python version ([Install Python](https://www.python.org/downloads/))
- Code Editor of your choice

---
### Basic Syntax

```python
print("Hello World!")

# = OUTPUT = #
# Hello World!
```
As we can see, python is very straight forward and easy to understand compared to other programing languages

Now let's learn about some basic statements

---

# Statements
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
        input("n = ") takes input from user and value is stored in variable x, range(0, x) generates numbers starting from 0 up to x-1, if i == 1: checks if i is equal to 1, continue skips the printing step if i is 1, print(i) prints the current value of i if it's not skipped. <br> `break` &larr; ends program <br> `continue` &larr; skips/continues a statement
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
