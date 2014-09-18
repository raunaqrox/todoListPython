def main():
	list = []
	top = -1
	while 1 :
		print "\n1.Add 2.Remove 3.Display 4.Sort [by name]\n"
		option = raw_input()
		if option == '':
			exit()
		else :
			if option == '1':
				print "Enter the item(s)"
				while 1:
					item = raw_input()
					if(item!=''):
						list.append(item)
					else:
						break
			elif option == '2':
				print "Enter the item(s)"
				while 1:
					item = raw_input()
					if(item!=''):
						list.append(item)
					else:
						break
			elif option == '3':
				
				print "Here's your todo list!"
				i = 0
				for item in list:
					i+=1
					print str(i)+". "+item
			
			elif option == '4':
				print "Enter the item(s)"
				while 1:
					item = raw_input()
					if(item!=''):
						list.append(item)
					else:
						break
if __name__== '__main__':
	main()
