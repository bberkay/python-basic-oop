<h2>Python Basic OOP examples</h2>
<p>Basic OOP examples in Python</p>
<hr>
<h3>Encapsilation</h3>
```python

class Bank:
    def __init__(self, age, money):
        self.age = age # this is accessible
        self.__money = money # "__" means private so this is inaccessible.

    def getMoney(self):
        return self.__money # but can return

#customer = Bank(20, 1000)
#print(customer.age) -> 20
#print(customer.money) is give -> AtributeError: 'Bank' object has no attribute 'money'
#print(customer.getMoney()) -> 1000

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

#monkey = Monkey()
#print(monkey) -> animal is created | monkey is created
#print(monkey.breathe()) -> animal is breathing
#print(monkey.climb()) -> monkey is climbing
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

#human = HumanEmployee()
#robot = RobotEmployee()
#print(human.work())
#print(human.eat())
#print(robot.work())
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

#vehicle = Vehicle()
#airplane = Airplane()        
#print(vehicle.toString()) -> Vehicle is moving
#print(airplane.toString()) -> Airplane is flying
```
