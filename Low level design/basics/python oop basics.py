# Private variables in python
# Encapsulation is bundling data (attributes) and methods inside a class and restricting direct access to some components.
class Account:
    __init__(self,balance):  # This is a constructor of this class
        self.__balance = balance

    creditAmount(self,amount):
        self.__balance += amount
    
    getBalance(self):
        print(self.balance)

account = Account(2000)
account.creditAmount(500)
print(account.__balance)    # This will throw error


# What is this self keyword
# -----> In Python, self is not a keyword, but it is a convention used to refer to the  current instance of a class. It allows you to access instance variables and methods from within the class.

# Key Points about self:
# It refers to the object itself.
# It must be the first parameter of instance methods.
# It is how Python differentiates between instance variables and local variables.


# Inheritance in Python 
# Inheritance allows one class to inherit the properties and methods of another.
class Animal:
    def speak(self):
        print('animal Speak')

class Dog(Animal):            # this is inheritance
    def speak(self):
        print("Dog barks")    # this is method overloading 


# Polymorphism in python
# Polymorphism allows different classes to have methods with the same name, but different behavior.
class Cat:
    def sound(self):
        print("meooowwww")

class Cow:
    def sound(self):
        print("Mooo moooo")


def make_sound(animal):
    animal.sound()

make_sound(Cat())  # Output: Meow
make_sound(Cow())  # Output: Moo


# Abstraction hides complex implementation details and shows only essential features. In Python, this is done using abc module (abstract base classes).

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):             # this instantiation is needed else error would be
                                # TypeError: Can't instantiate abstract class Circle without an implementation for abstract method 'area'
        return 3.14 * self.radius * self.radius

c = Circle(5)

# s = Shape() # error here due to abstractmethod
print(c.area())  # Output: 78.5
    

# @ decorators in python 

# 1. @abstractmethod
# Purpose: Define a method that must be implemented in a subclass.
# Where: Used inside abstract base classes.
# refer above example


# 2. @staticmethod
# Purpose: Define a method that does not need access to instance (self) or class (cls).
# Use case: Utility/helper methods.
class Math:
    @staticmethod
    def add(x, y):
        return x + y

print(Math.add(3, 4))  # Output: 7
# No self or cls is passed.


# 3. @classmethod
# Purpose: Define a method that has access to the class (cls) rather than the instance (self).
# Use case: Factory methods or modifying class-level data.
class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

print(Person.get_count())  # Output: 0
p1 = Person()
print(Person.get_count())  # Output: 1


# 4. @property
# Purpose: Allows you to define a method that can be accessed like an attribute.
# Use case: Read-only attributes or computed properties.
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

c = Circle(5)
print(c.area)  # Output: 78.5
# area is called like a variable, not a method.


# 5. Custom Decorators
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# print("Before function runs")
# print("Hello!")
# print("After function runs")