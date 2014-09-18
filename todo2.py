def display(list):
	i = 0
	for item in list:
		i+=1
		print str(i) + " " + item
def remove(list):
	print "Enter item number to remove"
	removeItemNumber = int(raw_input())
	del list[removeItemNumber-1]
	return list
def main():
	list = []
	while(1):
		print "1.Add 2.Delete 3.Display"
		option = raw_input()
		if option == '1':
			while 1:
				print "enter item to todolist"
				item = raw_input()
				if item  == '':
					break
				else:	
					list.append(item)
		elif option == '3':
			display(list)
		elif option == '2':
			display(list)
			list = remove(list)	
		elif option == '':
			break
	
if __name__ == '__main__':
	main()

