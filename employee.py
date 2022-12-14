"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary, numHours = 0, numContract = 0, commisionPerContract = 0, commissionPay = 0  ):
        self.name = name
        self.salary =salary
        #self.isMonthly = isMonthly
        self.numHours = numHours
        self.numContract = numContract
        self.commissionPay = commissionPay
        self.commisionPerContract = commisionPerContract

    def get_pay(self):
        totPayment =0

        #monthly  or hourly payment
        if self.numHours > 0:
            totPayment = self.numHours * self.salary
        else:
            totPayment = self.salary
        
        #with commision or without
        if self.numContract > 0 :
            totPayment += self.numContract * self.commisionPerContract
        else:
            totPayment += self.commissionPay
        
        return totPayment

    def __str__(self):
        statement = f'{self.name} works on' 
        if self.numHours > 0:
            statement += f' a contract of {self.numHours} hours at {self.salary}/hour'
        else:
            statement += f' a monthly salary of {self.salary}'
        
        if self.numContract > 0:
            statement +=  f' and receives a commission for {self.numContract} contract(s) at {self.commisionPerContract}/contract'
        elif self.commissionPay > 0:
            statement += f' and receives a bonus commission of {self.commissionPay}'

        statement += f'.  Their total pay is {self.get_pay()}.'
        return   statement 


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',25, 100)
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 4, 200)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',  25, 150, 3, 220)
print(jan.get_pay())
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 0, 0, 1500)
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, 120, 0, 0, 600 )
