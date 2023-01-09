# 0x0A. Python - Inheritance

Object-Oriented Programming (OOP) concept of `inheritance` with python.

Python has two built-in functions that work with inheritance:

- Use `isinstance()` to check an instance’s type: `isinstance(obj, int)` will be `True` only if `obj.__class__` is `int` or some class derived from `int`.

- Use  `issubclass()` to check class inheritance: `issubclass(bool, int)` is `True` since bool is a subclass of int. However, issubclass(float, int) is `False` since `float` is not a subclass of `int`.


Guiding questions:

- What is a superclass, baseclass or parent class
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use isinstance, issubclass, type and super built-in functions
