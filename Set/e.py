#20CE129
#Write a Python program to find the most common elements and their counts from list.

# element in a list

from itertools import count


def most_frequent(List):
	counter = 0
	num = List[0]
	
	for i in List:
		curr_frequency = List.count(i)
		if(curr_frequency> counter):
			counter = curr_frequency
			num = i

	print("frequant element is %d and counter for element is %d"%(num,counter))
     

List = [2, 1, 2, 2, 1, 3]
(most_frequent(List)) #this function will print most frequant element in list with their count.

#for dictionary and tuple convert both into list first then apply same function on them.

