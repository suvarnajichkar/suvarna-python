menu={'pizza':100,
	  'salad':40,
	  'bargur':60,
	  'manturian':30,
	  'coffee':20
	  }
print("welcome sir in our restaurent")
print("choose any item from this menu sir..")
for x, y in menu.items():
  print(x, y)


order_item = 0
item1 = input("enter the name of item you want to order= ")
if item1 in menu:
	order_item+=menu[item1]
	print(f"Your order {item1} has been added in order")
else:
	print(f"sorry,your order {item1} is not available yet")

another_item=input("do you want to order another item yes/no ")
item2=0
if another_item=='yes':
	item2= (input("enter your another order= "))
	if item2 in menu:
		order_item+=menu[item2]
		print(f"Your order {item2} has been added in order")
		print(f"your total bill is{order_item}")
	else:
		print("not available")


	





