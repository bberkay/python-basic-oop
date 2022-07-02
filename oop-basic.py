######################  PROCEDURAL #######################
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
"""
what if i want add volume function
i must add height for every rectangle and i must call function for
every rectangle with their length and width
this is annoying and an unnecessarily long process
"""
# example for volume
def getVolume(width, length, height):
    # volume calc
    pass

rect1_volume = getVolume(4, 4) # again 4, 4
print(rect1_volume)
rect2_volume = getVolume(2, 4) # again 2, 4 what if i don't remember length or accidently change the variable between functions ?
print(rect2_volume)
# and as seen i must create volume-area-perimeter variables for every rectangle

#########################  OOP ###########################
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

"""
what if i want add volume function
i add height for every rectangle object and i must call function for
every rectangle but i don't need with their length and width
"""
print(rect1.getVolume(6)) # just height
print(rect2.getVolume(8)) # just height
# and as seen i don't need create volume-area-perimeter variables for every rectangle i call them if i need them.
