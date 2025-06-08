# SOLID Principles in Python with Good and Bad Examples

# S - Single Responsibility Principle (SRP)
# Definition: A class should have only one reason to change, meaning it should have only one job or responsibility.

# ❌ Bad Example:
class Invoice:
    def calculate_total(self):
        print("Calculating total")

    def print_invoice(self):
        print("Printing invoice")

    def save_to_db(self):
        print("Saving to database")

# ✅ Good Example:
class Invoice:
    def calculate_total(self):
        print("Calculating total")

class InvoicePrinter:
    def print_invoice(self):
        print("Printing invoice")

class InvoiceSaver:
    def save_invoice(self):
        print("Saving to database")


# O - Open/Closed Principle (OCP)
# Definition: Software entities should be open for extension, but closed for modification.

# ❌ Bad Example:
class Discount:
    def calculate_discount(self, customer_type):
        if customer_type == "Gold":
            return 0.2
        elif customer_type == "Silver":
            return 0.1
        else:
            return 0

# ✅ Good Example:
class Discount:
    def calculate(self):
        return 0

class GoldDiscount(Discount):
    def calculate(self):
        return 0.2

class SilverDiscount(Discount):
    def calculate(self):
        return 0.1


# L - Liskov Substitution Principle (LSP)
# Definition: Subtypes must be substitutable for their base types without altering the correctness of the program.

# ❌ Bad Example:
class Bird:
    def fly(self):
        print("Flying")

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly")

# ✅ Good Example:
class Bird:
    def lay_eggs(self):
        print("Lays eggs")

class FlyingBird(Bird):
    def fly(self):
        print("Flying")

class Sparrow(FlyingBird):
    pass

class Ostrich(Bird):
    pass


# I - Interface Segregation Principle (ISP)
# Definition: A class should not be forced to implement interfaces it doesn't use.

# ❌ Bad Example:
class Machine:
    def print(self): pass
    def scan(self): pass
    def fax(self): pass

class OldPrinter(Machine):
    def print(self): print("Printing")
    def scan(self): raise NotImplementedError("Can't scan")
    def fax(self): raise NotImplementedError("Can't fax")

# ✅ Good Example:
class Printer:
    def print(self): pass

class Scanner:
    def scan(self): pass

class Fax:
    def fax(self): pass

class BasicPrinter(Printer):
    def print(self): print("Basic printing")

class MultiFunctionPrinter(Printer, Scanner, Fax):
    def print(self): print("Printing")
    def scan(self): print("Scanning")
    def fax(self): print("Faxing")


# D - Dependency Inversion Principle (DIP)
# Definition: High-level modules should not depend on low-level modules. Both should depend on abstractions.

# ❌ Bad Example:
class LightBulb:
    def turn_on(self):
        print("Bulb is on")

class Switch:
    def __init__(self):
        self.bulb = LightBulb()

    def operate(self):
        self.bulb.turn_on()

# ✅ Good Example:
class Switchable:
    def turn_on(self): pass

class LightBulb(Switchable):
    def turn_on(self):
        print("Bulb is on")

class Fan(Switchable):
    def turn_on(self):
        print("Fan is on")

class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self):
        self.device.turn_on()

# Usage
s1 = Switch(LightBulb())
s2 = Switch(Fan())
s1.operate()
s2.operate()
