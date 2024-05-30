phonebook={}

def add():
  name=input("enter name ")
  contactNo =input("enter contactNo ")
  if name not in phonebook :
    phonebook[name]=contactNo
  else:   
   print("alrady exist")
  
  
  
def search():
 name= input("enter what you want to search ")
 if name in phonebook:
  print(f"{name} : {phonebook[name]}")
 else:
  print("it is not present ")
  
def delete():
 userInput= input("enter what you want to delete ")
 if userInput in phonebook:
  del phonebook[userInput]

def displayAll():
  for x,y in phonebook.items():
   print(f"{x}:{y}")

while(True):
 print(" ")
 print("1.add\n2.search\n3.delete\n4.displayAll\nExit ")
 print("   ")
 number= input("enter number ")
 if number=="1":
  add()
 elif number=="2":
  search()
 elif number=="3":
  delete()
 elif number=="4":
  displayAll()
 elif number=="exit":
  break
 else:
  print("you entered wrong number again enter number")

 
