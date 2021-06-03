class cal1:
    n1=0
    n2=0
    n3=0
    def setdata(self):
        self.n1=int(input("Enter 1st number:"))
        self.n2=int(input("Enter 2nd number:"))
        self.n3=int(input("Enter 3rd number:"))

    def display(self):
        sum= self.n1 + self.n2 + self.n3
        print("The sum is:", sum)


sum = cal1()
sum.setdata()
sum.display()
