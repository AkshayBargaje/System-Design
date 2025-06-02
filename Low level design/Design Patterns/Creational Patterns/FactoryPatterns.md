Why we need Factory pattern?
---> Use when you want:
    You want to delegate object creation to a method/class.
    You have many subclasses of a product/interface.
    You want to decouple code from specific class instantiations.

Why to use it

1. Decouples Code
# ❌ Tight coupling:
animal = Dog()
# ✅ With factory:
animal = AnimalFactory.get_animal("dog")

2. Easy to add new Types
Just add a new subclass and register it — no need to change core logic.


3. 🔄 Implements Open/Closed Principle
Open for extension (new classes).
Closed for modification (no changes to existing code).


from abc import ABC, abstractmethod

# Step 1: Product Interface
class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

# Step 2: Concrete Products
class FileLogger(Logger):
    def log(self, message: str):
        with open("log.txt", "a") as f:
            f.write(f"[File] {message}\n")

class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f"[Console] {message}")

class EmailLogger(Logger):
    def log(self, message: str):
        print(f"[Email] Sending log: {message}")  # Simulate email

# Step 3: Factory Method
class LoggerFactory:
    @staticmethod
    def get_logger(logger_type: str) -> Logger:
        if logger_type == "file":
            return FileLogger()
        elif logger_type == "console":
            return ConsoleLogger()
        elif logger_type == "email":
            return EmailLogger()
        else:
            raise ValueError("Unknown logger type")

# Step 4: Usage
if __name__ == "__main__":
    logger_type = input("Choose logger (file/console/email): ").lower()
    logger = LoggerFactory.get_logger(logger_type)
    logger.log("Factory pattern implemented successfully!")
