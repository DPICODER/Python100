# Understanding Object-Oriented Programming (OOP) in Python

Object-Oriented Programming (OOP) is a programming paradigm that revolves around the concept of objects, which are instances of classes. Python is an object-oriented language, which means it supports the creation and manipulation of objects and classes.

## Key Concepts in OOP

### 1. Classes and Objects

- **Class**: A class is a blueprint for creating objects. It defines the attributes (data) and methods (functions) that characterize the objects.
  
- **Object**: An object is an instance of a class. It represents a specific entity in your program and can interact with other objects and classes.

### 2. Constructor (__init__)

- The `__init__` method is a special method in Python classes that initializes new objects. It is called automatically when a new instance of the class is created.
  
- It is used to initialize the attributes of the object and perform any necessary setup tasks.

### 3. Attributes

- Attributes are variables associated with a class or object. They represent the state or characteristics of the object.
  
- Attributes are accessed using dot notation (`object.attribute`).

### 4. Methods

- Methods are functions defined within a class that operate on objects of that class.
  
- They can modify the state of the object (attributes) and perform specific actions.

### 5. Inheritance

- Inheritance allows a class (subclass) to inherit properties and methods from another class (superclass).
  
- It promotes code reuse and establishes a hierarchy of classes.

### 6. Encapsulation

- Encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data within a single unit, i.e., the class.
  
- It hides the internal implementation details of the class and provides a clear interface for interacting with it.

### 7. Polymorphism

- Polymorphism allows objects of different classes to be treated as objects of a common superclass.
  
- It enables flexibility and dynamic behavior in your code.

## Example Usage

```python
class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001", "Varun")
user2 = User("002", "Sai")

user1.follow(user2)

print(user1.followers)  # Output: 1
print(user1.following)  # Output: 1
print(user2.followers)  # Output: 1
print(user2.following)  # Output: 0
```

In this example, we create a `User` class with attributes such as user ID, username, followers, and following. We also define a method `follow` to allow users to follow each other.
