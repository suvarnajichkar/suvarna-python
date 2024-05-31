task=[]
num=int(input("enter how many task you want "))
for i in range(1,num+1):
	taskName=input(f"enter task {i} =")
	task.append(taskName)
print("total task are\n")
print(task)
print("\n")

while True:
	print("1-Add\n2-update\n3-delete\n4-view\n5-Exit\n")
	get_input=int(input("enter number "))

	#  adding task in list
	if get_input==1:
		addTask=input("what do you want to add ")
		if addTask  not in task:
			task.append(addTask)
			print("adding successfully")
		else:
			print("already inside the list ")

	# update in the list
	elif get_input==2:
		oldTask=input("enter which you want  to update ")
		if oldTask in task:
			newTask=input("enter what you want to update ")
			index=task.index(oldTask)
			task[index]=newTask
			print("update successfully")

		else:
			print("this type of task not present in the list ")

	# delete from list
	elif get_input==3:
		forDelete=input("enter what you want to delete ")
		if forDelete in task:
			index=task.index(forDelete)
			del task[index]
			# task.remove(forDelete)
			print("delete successfully")
		else:
			print("this type of task not present in the list ")

	# show all the task which present inside the list
	elif get_input==4:
		print(task)
		

	# for the exit
	elif get_input==5:
		break

	else:
		print("inavalid input")

		



		
