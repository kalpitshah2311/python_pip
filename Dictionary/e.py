#20CE129
#Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {} #initializing dictionary with empty braces
for d in (dic1, dic2, dic3): dic4.update(d) #this loop will concatenate dictionaries one by one
print(dic4) #this will print the updated dictionary