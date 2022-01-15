#20CE129
#Write a Python program to sum all the items in a dictionary.

# Function to print sum
def returnSum(myDict):
	
	list = []
	for i in myDict:
		list.append(myDict[i])
	final = sum(list)
	
	return final


dict = {'a': 100, 'b':200, 'c':300}
print("Sum :", returnSum(dict)) #this will print the sum of all elements in the dictionary.
