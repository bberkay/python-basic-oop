<h2>Basic OOP with easy examples in Python for beginners</h2>
<ol>
    <li><a href = "https://github.com/bberkay/python-basic-oop/blob/main/README.md#oop">OOP</a></li>
    <li><a href = "https://github.com/bberkay/python-basic-oop/blob/main/README.md#principles-of-oop">OOP Principles</a></li>
</ol>
<hr>
<h3>OOP</h3>

<hr>
<h3>Principles of OOP</h3>
<ul>
    <li>Encapsulation</li>
    <li>Inheritance</li>
    <li>Abstraction</li>
    <li>Polymorphism</li>
</ul>
<h3>Encapsilation</h3>

```python
class Bank:
    def __init__(self, age, money):
        self.age = age # this is accessible
        self.__money = money # "__" means private so this is inaccessible.

    def getMoney(self):
        return self.__money # but can return

customer = Bank(20, 1000)
print(customer.age)        # is give -> 20
print(customer.money)      # is give -> AtributeError: 'Bank' object has no attribute 'money'
print(customer.getMoney()) # is give -> 1000
```
<br>
<h3>Inheritance</h3>

```python
class Animal:
    def __init__(self):
        print("animal is created")

    def movement(self):
        print("animal moving")

    def breathe(self):
        print("animal breathing")

class Monkey(Animal):
    def __init__(self):
        super().__init__() # run animal in __init__ method -> animal is created

        print("monkey is created")

    def climb(self):
        print("monkey climbing")

monkey = Monkey()
print(monkey)           # is give -> animal is created & monkey is created
print(monkey.breathe()) # is give -> animal is breathing
print(monkey.climb())   # is give -> monkey is climbing
```
<br>
<h3>Abstraction</h3>

```python
from abc import ABC, abstractmethod # abstaction is imported

class Company(ABC):
    @abstractmethod
    def work(self): # abstactmethod is made it mandatory this method because robot and human must working
        pass
    
    def eat(self): # this is not mandatory because the robot doesn't have to eat but human does
        pass

class HumanEmployee(Company):
    def work(self):
        print("human working")

    def eat(self):
        print("human eating")

class RobotEmployee(Company):
    def work(self):
        print("robot working")

human = HumanEmployee()
robot = RobotEmployee()
print(human.work()) # is give -> human working
print(human.eat())  # is give -> human eating
print(robot.work()) # is give -> robot working
```
<br>
<h3>Polymorphism</h3>

```python
class Vehicle:
    def toString(self):
        print("Vehicle is moving")

class Airplane(Vehicle):
    def toString(self): # this method override toString method in Vehicle
        print("Airplane is flying")

vehicle = Vehicle()
airplane = Airplane()        
print(vehicle.toString())  # is give -> Vehicle is moving
print(airplane.toString()) # is give -> Airplane is flying
```
