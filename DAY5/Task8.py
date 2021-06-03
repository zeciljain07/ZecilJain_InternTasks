class publisher:

     def Name(self):
         self.title=input("Enter the title of the book:")

class book(publisher):

    def data(self):
        self.pageNum=int(input("Enter the number of pages of the book:"))

class tape(publisher):

    def timeForPlaying(self):
        self.time=float(input("Enter the time for playing:"))

a=book()
b=tape()

a.Name()
a.data()
b.timeForPlaying()
