# Object-Oriented Programming (OOP) in Python

This note provides a detailed explanation of Object-Oriented Programming (OOP) concepts in Python, adapted from the provided Java-based document. It covers key OOP principles such as **Inheritance**, **Polymorphism**, **Encapsulation**, **Abstraction**, and **Interfaces** (emulated in Python using abstract base classes). Each section includes definitions, explanations, tables, and Python code examples, with references to the original document's content and additional clarifications for Python-specific implementations.

---

## 1. Inheritance

### Definition
Inheritance is a mechanism where a new class (subclass or derived class) is created from an existing class (superclass or base class), inheriting its attributes and methods. This promotes code reusability and establishes a hierarchical relationship between classes.

### Key Points (Ref: Page 1)
- In Python, inheritance is achieved by specifying the parent class in parentheses during class definition.
- It provides **code reusability** by allowing subclasses to use the properties of the superclass.
- Private members (denoted by double underscores `__`) are not directly accessible in subclasses.
- A subclass inherits all features of the superclass, and objects are typically created from the subclass.
- Method overloading is not directly supported in Python (unlike Java), but similar functionality can be achieved using default arguments or variable-length arguments.

### Types of Inheritance (Ref: Pages 1-2, 4-8)
1. **Single Inheritance**: One superclass and one subclass.
2. **Multi-level Inheritance**: A chain of inheritance where a subclass becomes the superclass for another class.
3. **Hierarchical Inheritance**: Multiple subclasses inherit from a single superclass.
4. **Multiple Inheritance**: A subclass inherits from multiple superclasses (supported in Python, unlike Java's class-based multiple inheritance).

**Note**: Python supports multiple inheritance directly through classes, unlike Java, which restricts multiple inheritance to interfaces (Ref: Page 9). Python avoids the "diamond problem" by using the **Method Resolution Order (MRO)**.

### Access Modifiers in Python (Ref: Page 2)
Python does not have strict access modifiers like Java (`private`, `protected`, `public`). Instead, it uses naming conventions:
- **Public**: No prefix (e.g., `variable`).
- **Protected**: Single underscore prefix (e.g., `_variable`) – a convention indicating it should not be accessed directly.
- **Private**: Double underscore prefix (e.g., `__variable`) – name mangling restricts direct access.

| Modifier | Access in Subclass (Same Module) | Access in Subclass (Different Module) |
|----------|----------------------------------|---------------------------------------|
| Private (`__variable`) | Not directly accessible | Not directly accessible |
| Protected (`_variable`) | Accessible (by convention) | Accessible (by convention) |
| Public (`variable`) | Accessible | Accessible |

### Examples

#### Single Inheritance (Ref: Pages 3-4)
```python
class Sum:
    def __init__(self, a, b):
        self._a = a  # Protected attributes
        self._b = b
    def addition(self):
        print(f"Sum: {self._a + self._b}")

class Subtraction(Sum):
    def __init__(self, a, b):
        super().__init__(a, b)  # Call parent constructor
    def subtraction(self):
        print(f"Subtraction: {self._a - self._b}")

# Main
if __name__ == "__main__":
    obj = Subtraction(10, 5)
    obj.addition()      # Output: Sum: 15
    obj.subtraction()   # Output: Subtraction: 5
```

#### Multi-level Inheritance (Ref: Pages 4-5)
```python
class Sum:
    def __init__(self, a, b):
        self._a = a
        self._b = b
    def addition(self):
        print(f"Sum: {self._a + self._b}")

class Sub(Sum):
    def subtraction(self):
        print(f"Subtraction: {self._a - self._b}")

class Multi(Sub):
    def multiplication(self):
        print(f"Multiplication: {self._a * self._b}")

class Div(Multi):
    def division(self):
        if self._b != 0:
            print(f"Division: {self._a / self._b}")
        else:
            print("Division by zero is not allowed.")

# Main
if __name__ == "__main__":
    obj = Div(20, 5)
    obj.addition()       # Output: Sum: 25
    obj.subtraction()    # Output: Subtraction: 15
    obj.multiplication() # Output: Multiplication: 100
    obj.division()       # Output: Division: 4.0
```

#### Hierarchical Inheritance (Ref: Pages 6-8)
```python
class Sum:
    def __init__(self, a, b):
        self._a = a
        self._b = b
    def addition(self):
        print(f"Sum: {self._a + self._b}")

class Sub(Sum):
    def subtraction(self):
        print(f"Subtraction: {self._a - self._b}")

class Multi(Sum):
    def multiplication(self):
        print(f"Multiplication: {self._a * self._b}")

class Div(Sum):
    def division(self):
        if self._b != 0:
            print(f"Division: {self._a / self._b}")
        else:
            print("Division by zero is not allowed.")

# Main
if __name__ == "__main__":
    print("Using Sub class:")
    sub_obj = Sub(20, 10)
    sub_obj.addition()      # Output: Sum: 30
    sub_obj.subtraction()   # Output: Subtraction: 10

    print("\nUsing Multi class:")
    multi_obj = Multi(20, 10)
    multi_obj.addition()      # Output: Sum: 30
    multi_obj.multiplication() # Output: Multiplication: 200

    print("\nUsing Div class:")
    div_obj = Div(20, 10)
    div_obj.addition()    # Output: Sum: 30
    div_obj.division()    # Output: Division: 2.0
```

#### Multiple Inheritance (Ref: Pages 9-10, 39-41)
```python
class Athlete:
    def play_sport(self):
        pass

class Musician:
    def play_instrument(self):
        pass

class Person(Athlete, Musician):
    def __init__(self, name):
        self.name = name
    def play_sport(self):
        print(f"{self.name} is playing football.")
    def play_instrument(self):
        print(f"{self.name} is playing the guitar.")

# Main
if __name__ == "__main__":
    john = Person("John")
    john.play_sport()       # Output: John is playing football.
    john.play_instrument()  # Output: John is playing the guitar.
```

### Additional Explanation
- **Python's MRO**: Python uses the C3 linearization algorithm to resolve method calls in multiple inheritance. You can inspect the MRO using `ClassName.__mro__`.
- Unlike Java, Python does not restrict multiple inheritance, making it more flexible but requiring careful design to avoid conflicts.
- The `super()` function in Python is used to call methods from the parent class, and it dynamically resolves the correct parent based on the MRO.

---

## 2. Polymorphism

### Definition
Polymorphism allows objects to take multiple forms, enabling methods to perform different tasks based on the object calling them. It comes from the Greek words "poly" (many) and "morph" (forms) (Ref: Page 11).

### Types of Polymorphism (Ref: Pages 11-12)
1. **Compile-Time Polymorphism (Static Binding)**: Achieved through method overloading or operator overloading.
2. **Runtime Polymorphism (Dynamic Binding)**: Achieved through method overriding.

### Key Points
- Python does not support method overloading directly (unlike Java). Instead, it uses default arguments, variable-length arguments, or type checking to achieve similar functionality.
- Method overriding is fully supported, where a subclass provides a different implementation of a method defined in the superclass.
- Python’s dynamic typing inherently supports polymorphism, as objects are resolved at runtime.

### Examples

#### Method Overloading (Emulated in Python) (Ref: Pages 11-12)
```python
class Calculator:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        return a + b

# Main
if __name__ == "__main__":
    calc = Calculator()
    print(f"Sum of two integers: {calc.add(10, 20)}")      # Output: Sum of two integers: 30
    print(f"Sum of three integers: {calc.add(10, 20, 30)}") # Output: Sum of three integers: 60
```

#### Method Overriding (Ref: Pages 12-13)
```python
class Animal:
    def sound(self):
        print("This is a generic animal sound.")

class Dog(Animal):
    def sound(self):
        print("The dog barks.")

class Cat(Animal):
    def sound(self):
        print("The cat meows.")

# Main
if __name__ == "__main__":
    my_animal = Dog()
    my_animal.sound()  # Output: The dog barks.
    my_animal = Cat()
    my_animal.sound()  # Output: The cat meows.
```

#### Real-Life Example (Ref: Page 14)
```python
class Payment:
    def pay(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            print(f"Paid((*args), 2) and isinstance(args[1], float):
            print(f"Paid {args[1]} using UPI ID: {args[0]}")
        else:
            print("Invalid payment method.")

# Main
if __name__ == "__main__":
    payment = Payment()
    payment.pay("1234-5678-9012-3456")           # Output: Paid using Credit Card: 1234-5678-9012-3456
    payment.pay(123456789)                       # Output: Paid using Debit Card: 123456789
    payment.pay("user@upi", 500.0)               # Output: Paid 500.0 using UPI ID: user@upi
```

### Key Features of Polymorphism (Ref: Page 15)
1. **Flexibility**: A single interface can work with different object types.
2. **Extensibility**: New subclasses can be added without modifying existing code.
3. **Maintainability**: Code is easier to maintain and extend.

### Method Checking and Overriding Rules (Ref: Page 16)
1. Check if the method exists in the superclass.
2. If it exists, determine if it is overridden in the subclass.
3. Call the subclass method if overridden; otherwise, call the superclass method.

```python
class Superclass:
    def display(self):
        print("Superclass method.")

class Subclass(Superclass):
    def display(self):
        print("Subclass method.")

# Main
if __name__ == "__main__":
    obj1 = Superclass()
    obj1.display()  # Output: Superclass method.
    obj2 = Subclass()
    obj2.display()  # Output: Subclass method.
```

---

## 3. Super Keyword (Python Equivalent)

### Explanation
In Python, the `super()` function is used to access methods and attributes of the parent class, similar to Java’s `super` keyword (Ref: Pages 18-22). It is commonly used to:
- Call the parent class constructor.
- Access parent class methods or variables when overridden or shadowed.

### Uses of `super()` (Ref: Page 21)
1. **Accessing Parent Class Variables**: Differentiate between parent and child class variables with the same name.
2. **Calling Overridden Methods**: Invoke the parent class version of an overridden method.
3. **Invoking Parent Class Constructor**: Initialize the parent class during subclass instantiation.

### Examples

#### Accessing Parent Class Variables (Ref: Page 18)
```python
class Parent:
    name = "Parent Class"

class Child(Parent):
    name = "Child Class"
    def display_names(self):
        print(f"Child Name: {self.name}")
        print(f"Parent Name: {super().name}")

# Main
if __name__ == "__main__":
    obj = Child()
    obj.display_names()
    # Output:
    # Child Name: Child Class
    # Parent Name: Parent Class
```

#### Accessing Parent Class Methods (Ref: Page 19)
```python
class Parent:
    def show(self):
        print("This is the Parent class method.")

class Child(Parent):
    def show(self):
        print("This is the Child class method.")
    def display(self):
        super().show()  # Call parent method
        self.show()     # Call child method

# Main
if __name__ == "__main__":
    obj = Child()
    obj.display()
    # Output:
    # This is the Parent class method.
    # This is the Child class method.
```

#### Calling Parent Class Constructor (Ref: Page 20)
```python
class Parent:
    def __init__(self, message):
        print(f"Parent Constructor: {message}")

class Child(Parent):
    def __init__(self, message):
        super().__init__(message)  # Call parent constructor
        print(f"Child Constructor: {message}")

# Main
if __name__ == "__main__":
    obj = Child("Hello from the constructor!")
    # Output:
    # Parent Constructor: Hello from the constructor!
    # Child Constructor: Hello from the constructor!
```

---

## 4. Encapsulation

### Definition
Encapsulation bundles data (attributes) and methods into a single unit (class) while restricting direct access to some components to ensure data security and control (Ref: Page 23).

### Key Points
- Attributes should be private or protected to prevent unauthorized access.
- Public methods (getters and setters) provide controlled access to attributes.
- Python uses naming conventions (`_variable` for protected, `__variable` for private) to enforce encapsulation.

### Example (Ref: Pages 23-26)
```python
class BankAccount:
    def __init__(self, account_holder_name, initial_balance):
        self.__account_holder_name = account_holder_name  # Private
        self.__balance = 0
        if initial_balance > 0:
            self.__balance = initial_balance
        else:
            print("Initial balance must be positive.")
    
    # Getter for account holder name
    def get_account_holder_name(self):
        return self.__account_holder_name
    
    # Setter for account holder name
    def set_account_holder_name(self, name):
        self.__account_holder_name = name
    
    # Getter for balance
    def get_balance(self):
        return self.__balance
    
    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    
    # Withdraw method
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}, Remaining Balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

# Main
if __name__ == "__main__":
    account = BankAccount("John Doe", 1000)
    print(f"Account Holder: {account.get_account_holder_name()}")
    print(f"Initial Balance: {account.get_balance()}")
    account.set_account_holder_name("Alice Johnson")
    print(f"Updated Account Holder: {account.get_account_holder_name()}")
    account.deposit(1500)
    account.withdraw(2000)
    account.withdraw(6000)
    # Output:
    # Account Holder: John Doe
    # Initial Balance: 1000
    # Updated Account Holder: Alice Johnson
    # Deposited: 1500, New Balance: 2500
    # Withdrawn: 2000, Remaining Balance: 500
    # Insufficient balance or invalid amount.
```

---

## 5. Abstraction

### Definition
Abstraction hides implementation details and exposes only the essential functionality to the user, reducing complexity and improving maintainability (Ref: Page 27).

### Advantages
- **Security**: Internal workings are hidden.
- **Enhancement**: Modifications can be made without affecting the user interface.

### Implementation in Python
Python implements abstraction using:
1. **Abstract Base Classes (ABCs)**: Provided by the `abc` module.
2. **Interfaces**: Emulated using ABCs with abstract methods.

### Abstract Class
An abstract class cannot be instantiated and may contain abstract (unimplemented) and concrete (implemented) methods. Subclasses must implement all abstract methods (Ref: Page 27).

### Example (Ref: Pages 29-32)
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sounds(self):
        pass
    @abstractmethod
    def speed(self):
        pass

class Cat(Animal):
    def sounds(self):
        print("Mecooowww")
    def speed(self):
        print("30 mph")

class Lion(Animal):
    def sounds(self):
        print("Roaaaaaaar")
    def speed(self):
        print("65 mph")

# Main
if __name__ == "__main__":
    cat = Cat()
    lion = Lion()
    cat.sounds()  # Output: Mecooowww
    lion.sounds() # Output: Roaaaaaaar
```

#### Abstract Method Example
```python
from abc import ABC, abstractmethod

class Students(ABC):
    def __init__(self):
        print("All Students: ")
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def id(self):
        pass

class Rahim(Students):
    def name(self):
        print("Name: Rahim")
    def id(self):
        print(f"ID: {199021216}")

# Main
if __name__ == "__main__":
    s = Rahim()
    s.name()  # Output: All Students: \n Name: Rahim
    s.id()    # Output: ID: 199021216
```

---

## 6. Interfaces (Emulated in Python)

### Definition
In Python, interfaces are emulated using abstract base classes (ABCs) from the `abc` module. An interface defines a contract of methods that implementing classes must provide (Ref: Page 33).

### Key Points
- All methods in an interface are abstract and implicitly public.
- Variables in an interface are static and final (constants).
- Implementing classes must override all interface methods.
- Python does not have a separate `interface` keyword like Java; ABCs serve this purpose.

### Example (Ref: Pages 33-38)
```python
from abc import ABC, abstractmethod

class Client(ABC):
    @abstractmethod
    def input(self):
        pass
    @abstractmethod
    def output(self):
        pass

class Developer(Client):
    def __init__(self):
        self.name = ""
        self.salary = 0.0
    def input(self):
        self.name = input("Enter Username: ")
        self.salary = float(input("Enter Salary: $"))
    def output(self):
        print(f"Username: {self.name}")
        print(f"Salary: ${self.salary}")

# Main
if __name__ == "__main__":
    g = Developer()
    g.input()
    g.output()
    # Example Output (user input: "John", "50000"):
    # Enter Username: John
    # Enter Salary: $50000
    # Username: John
    # Salary: $50000
```

### Multiple Inheritance Using Interfaces (Ref: Pages 39-41)
```python
from abc import ABC, abstractmethod

class Athlete(ABC):
    @abstractmethod
    def play_sport(self):
        pass

class Musician(ABC):
    @abstractmethod
    def play_instrument(self):
        pass

class Person(Athlete, Musician):
    def __init__(self, name):
        self.name = name
    def play_sport(self):
        print(f"{self.name} is playing football.")
    def play_instrument(self):
        print(f"{self.name} is playing the guitar.")

# Main
if __name__ == "__main__":
    john = Person("John")
    john.play_sport()       # Output: John is playing football.
    john.play_instrument()  # Output: John is playing the guitar.
```

### Why Use ABCs for Interfaces?
- **Contract Enforcement**: Ensures all implementing classes provide required methods.
- **Flexibility**: Supports multiple inheritance safely.
- **Clarity**: Clearly defines the expected behavior without implementation details.

---

## Additional Notes
- **Python vs. Java Differences**:
  - Python’s dynamic typing and lack of strict access modifiers make it more flexible but less rigid than Java.
  - Method overloading is emulated in Python using flexible argument handling.
  - Python’s `abc` module provides a robust way to emulate Java interfaces.
- **Best Practices**:
  - Use protected attributes (`_variable`) for internal use within classes and subclasses.
  - Use private attributes (`__variable`) sparingly, as name mangling can complicate code.
  - Leverage `super()` for clean inheritance and method resolution.
  - Use ABCs for defining interfaces to ensure contract enforcement.

This comprehensive note adapts the Java-based OOP concepts to Python, maintaining the structure and examples from the original document while incorporating Python-specific conventions and features.