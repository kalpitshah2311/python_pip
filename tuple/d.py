#20CE129
#Write a Python program to convert a tuple to a string.
def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str
 
 

tuple = ('k', 'a', 'l', 'p', 'i','t')
str = convertTuple(tuple)
print(str)