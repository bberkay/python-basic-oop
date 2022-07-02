<h1>Basic OOP with easy examples in Python for beginners</h1>
<ol>
    <li><a href = "https://github.com/bberkay/python-basic-oop#oop">OOP</a></li>
    <li><a href = "https://github.com/bberkay/python-basic-oop#principles-of-oop">OOP Principles</a></li>
</ol>
<hr>
<h2>OOP</h2>
<h3>Procedural</h3>

```python
def getArea(width, length):
    return width * length

def getPerimeter(width, length):
    return 2*(width + length)

# First Rectangle width 4, length 4
rect1_area = getArea(4, 4)
print(rect1_area) # is give -> 16
rect1_perimeter = getPerimeter(4,4)
print(rect1_perimeter) # is give -> 16

# Second Rectangle width 2, length 4
rect2_area = getArea(2,4)
print(rect2_area) # is give -> 8
rect2_perimeter = getPerimeter(2,4)
print(rect2_perimeter) # is give -> 12
```
<ul><li>what if i want add volume function i must add height for every rectangle and i must call function for every rectangle with their length and width this is annoying and an unnecessarily long process</li></ul>

```python
# example for volume
def getVolume(width, length, height):
    # volume calc
    pass

rect1_volume = getVolume(4, 4) # again 4, 4
print(rect1_volume)
rect2_volume = getVolume(2, 4) # again 2, 4 what if i don't remember length or accidently change the variable between functions ?
print(rect2_volume)
# and as seen i must create volume-area-perimeter variables for every rectangle
```
<br>
<h3>OOP</h3>

```python
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def getArea(self):
        return self.width * self.length

    def getPerimeter(self):
        return 2*(self.width + self.length)

    # example for volume
    def getVolume(self, height):
        # volume calc
        pass

# First Rectangle width 4, length 4
rect1 = Rectangle(4, 4)
print(rect1.getArea())      # is give -> 16
print(rect1.getPerimeter()) # is give -> 16

# Second Rectangle width 2, length 4
rect2 = Rectangle(2, 4)
print(rect2.getArea())      # is give -> 8
print(rect2.getPerimeter()) # is give -> 12
```
<ul><li>what if i want add volume function i add height for every rectangle object and i must call function for every rectangle but i don't need with their length and width</li></ul>

```python
print(rect1.getVolume(6)) # just height
print(rect2.getVolume(8)) # just height
# and as seen i don't need create volume-area-perimeter variables for every rectangle i call them if i need them.
```
<hr>
<h2>Principles of OOP</h2>
<ul>
    <li>Encapsulation</li>
    <li>Inheritance</li>
    <li>Abstraction</li>
    <li>Polymorphism</li>
</ul>
<h3>Encapsulation</h3>

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
