class Bank:
	def __init__(self,account_holder,account_no,balance=0.00):
		self.account_holder=account_holder
		self.account_no=account_no
		self.balance=balance

	# deposite amount
	def deposite(self):
		amount=int(input("enter the amount for deposite "))
		if amount>0:
			self.balance+=amount
			print(f"deposite amount is {amount}  ")
		else:
			print(f"amount should be positive ")

		
	# withdraw amount
	def withdraw(self):
		amount=int(input("enter amount for withdraw "))
		if amount>0 and self.balance>amount:
			self.balance-=amount
			print(f"withdraw amount are {amount}")
		elif amount>self.balance:
			print("insufficient amount ")
		else:
			print("amount should be positive ")

	# chek balance
	def check_balance(self):
		print(f"total balance are {self.balance} ")

# main function
account_holder=input("enter your  name ")
account_no=int(input("enter your account no. "))
obj1=Bank(account_holder,account_no)

print("1.deposite\n2.withdraw\n3.check_balance\n4.Exit")

while(True):
	num=int(input("enter the no. for Transaction "))
	if num==1:
		obj1.deposite()
	elif num==2:
		obj1.withdraw()
	elif num==3:
		obj1.check_balance()
	elif num==4:
		print("Exit")
		break
	else:
		print("wrong number please put correct")






