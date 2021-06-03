class cal6:
    a=0
    area=0

    def setdata(self):
        self.a=float(input("Enter the length of the square's side:"))

    def area(self):
        self.area=self.a ** 2

    def display(self):
        print("The area of the square is:" + str(self.area))


ar=cal6()
ar.setdata()
ar.area()
ar.display()
