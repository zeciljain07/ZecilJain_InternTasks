class cal4:
    n=0
    square=0

    def setdata(self):
        self.n=int(input("Enter the number:"))

    def display(self):
        self.square = (self.n)**2
        return self.square

sq=cal4()
sq.setdata()
print(sq.display())
