# 01-Python-Basics - Python Architecture

Welcome to this comprehensive guide on **Python Architecture**. This module is designed to take you from a complete beginner to an industry-level python expert.

---

## 1. Theory
Python is a compiled-interpreted hybrid language. Source code (.py) is compiled to bytecode (.pyc) which is then executed on the Python Virtual Machine (PVM).

---

## 2. Internals
CPython uses a compiler stage to generate bytecode from the AST. The bytecode interpreter loop is a massive switch statement inside the eval loop (`ceval.c`).

---

## 3. Syntax
```python
# Execution Flow Check
import sys
print(sys.version_info)
```

---

## 4. Beginner Examples
```python
# Simple check
if __name__ == '__main__':
    print('Running script directly')
```

---

## 5. Intermediate Examples
```python
import dis

def add(a, b):
    return a + b

# Disassemble bytecode
dis.dis(add)
```

---

## 6. Advanced Examples
```python
import sys
import gc

class Node:
    pass

a = Node()
b = Node()
a.ref = b
b.ref = a # Circular reference

print('Ref count of a:', sys.getrefcount(a))
gc.collect() # Force run GC collector
```

---

## 7. Production Examples
```python
import sys
import logging

logging.basicConfig(level=logging.INFO)

def check_interpreter_env():
    logging.info('CPython version: %s', sys.version)
    logging.info('Execution platform: %s', sys.platform)
    logging.info('Recursion limit: %s', sys.getrecursionlimit())
```

---

## 8. Exercises
- **Exercise 1:** Write a python function implementing Python Architecture.
- **Exercise 2:** Debug alignment issues or variable scopes in the implementation.

---

## 9. Solutions
- **Solution 1:** Write code matching the syntax guidelines.
- **Solution 2:** Wrap scopes using local context keywords or context managers.

---

## 10. Interview Questions
- **Q1:** What is CPython?
  *Answer:* It is the default, reference implementation of Python written in C. It compiles Python scripts to bytecode and executes them on a stack-based virtual machine.

---

## 11. Best Practices
Understand ref counts and garbage collection cycles to write memory-efficient applications.

---

## 12. Common Mistakes
- **Mistake:** Relying on instant object deletion via garbage collector for circular references.

---

## 13. Performance Notes
Run python with -O flag to strip assert statements and optimize bytecode compiler passes.

---

## 14. Security Notes
Never use sys.setrecursionlimit to unreasonably high numbers as it could cause C-level stack overflows.

---

## 15. Summary
In this chapter, we explored Python Architecture, reviewing internals, execution configurations, and production code snippets.
