# 05-OOP - SOLID Principles

Welcome to this comprehensive guide on **SOLID Principles**. This module is designed to take you from a complete beginner to an industry-level python expert.

---

## 1. Theory
SOLID is a set of five design principles to make software designs more understandable, flexible, and maintainable.

---

## 2. Internals
Inside CPython, SOLID Principles is parsed into an AST (Abstract Syntax Tree), compiled to Python bytecode, and executed on the virtual machine stack loop.

---

## 3. Syntax
```python
# S - Single Responsibility
# O - Open/Closed
# L - Liskov Substitution
# I - Interface Segregation
# D - Dependency Inversion
```

---

## 4. Beginner Examples
```python
# Single responsibility example
class Report:
    def get_data(self):
        return 'Report data'

class ReportPrinter:
    def print(self, report):
        print(report.get_data())
```

---

## 5. Intermediate Examples
```python
from abc import ABC, abstractmethod

# Open/Closed example
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
```

---

## 6. Advanced Examples
```python
from abc import ABC, abstractmethod

# Dependency Inversion Example
class MessageSender(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailSender(MessageSender):
    def send(self, message):
        print('Sending Email:', message)

class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender
    def notify(self, message):
        self.sender.send(message)
```

---

## 7. Production Examples
```python
# Fully conformant SOLID system
from abc import ABC, abstractmethod

class OrderRepository(ABC):
    @abstractmethod
    def save(self, order):
        pass

class DatabaseOrderRepository(OrderRepository):
    def save(self, order):
        # Save order logic
        pass

class OrderManager:
    def __init__(self, repo: OrderRepository):
        self.repo = repo
    def process_order(self, order):
        self.repo.save(order)
```

---

## 8. Exercises
- **Exercise 1:** Write a python function implementing SOLID Principles.
- **Exercise 2:** Debug alignment issues or variable scopes in the implementation.

---

## 9. Solutions
- **Solution 1:** Write code matching the syntax guidelines.
- **Solution 2:** Wrap scopes using local context keywords or context managers.

---

## 10. Interview Questions
- **Q1:** Explain Liskov Substitution Principle?
  *Answer:* Subtypes must be substitutable for their base types without breaking the correctness of the application.

---

## 11. Best Practices
Code to interfaces (Abstract Base Classes) rather than concrete implementations.

---

## 12. Common Mistakes
- **Mistake:** Creating massive, monolithic classes carrying dozens of responsibilities.

---

## 13. Performance Notes
Abstract interfaces introduce very minor method call overhead, which is negligible compared to clean architecture benefits.

---

## 14. Security Notes
Isolate user authentication logic from database query managers.

---

## 15. Summary
In this chapter, we explored SOLID Principles, reviewing internals, execution configurations, and production code snippets.
