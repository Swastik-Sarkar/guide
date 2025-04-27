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
          if <logic>:
            <output code>
          elif <logic>:
            <else if output code>
          else:
            <else output code>
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
          while <logic>:
            <output code>
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
        here it forms a **loop** (we will learn about that a little later), in simple terms... Since we know 1 + 1 = 2, the while statement keeps on printing "yes" infinitly until stopped by the user
        
