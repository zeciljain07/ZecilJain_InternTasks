import math

class cal2:

    radius=0
    area=0

    def setdata(self):
        self.radius=float(input("Enter the radius of the circle:"))

    def area(self):
        self.area= math.pi*(self.radius**2)

    def display(self):
        print("The area of the circle with radius:" + str(self.radius) + "\nis :"+ str(self.area))

circle_area=cal2()
circle_area.setdata()
circle_area.area()
circle_area.display()
