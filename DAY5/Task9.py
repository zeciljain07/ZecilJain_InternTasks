class scheme:

    def Scheme(self):
        self.scheme_id=int(input("Enter the Scheme Id : "))
        self.scheme_name=input("Enter the Scheme Name : ")
        self.outgoing_rate=float(input("Enter the Outgoing Rate : "))
        self.message_charge=float(input("Enter the Message Charge : "))

class customer(scheme):

    def cust_data(self):
        self.cust_id=int(input("Enter the Customer Id : "))
        self.cust_name=input("Enter the Customer Name : ")
        self.mobile_no=int(input("Enter the Mobile Number : "))

c=customer()

c.Scheme()
c.cust_data()
