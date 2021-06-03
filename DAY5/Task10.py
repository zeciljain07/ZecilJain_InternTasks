class arith:
    n1=0
    n2=0

    def __init__(self, n1, n2):
        self.n1=n1
        self.n2=n2

    def add(self):
        self.add= self.n1 + self.n2
        print("The sum of two numbers is: ", self.add)

    def sub(self):
        self.sub= self.n1 - self.n2
        print("The subtraction of two numbers is: ", self.sub)

    def mul(self):
        self.mul= self.n1 * self.n2
        print("The multiplication of the two numbers is: ", self.mul)

ar=arith(12,5)
ar.add()
ar.sub()
ar.mul()
