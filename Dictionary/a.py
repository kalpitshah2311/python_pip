#20CE129
# Write a Python script to check whether a given key already exists in a dictionary.

def checkKey(dict, key):
	
	if key in dict.keys():
		print("Present, ", end =" ")
		print("value =", dict[key])
	else:
		print("Not present")


dict = {'a': 100, 'b':200, 'c':300}

key = 'b' 
checkKey(dict, key) #if key is present then it will print present as well as the sum
                    #else it will print Not Present
key = 'w'
checkKey(dict, key) 
