#20ce129
#Kalpit Shah
# Find runner-up from given list of scores.

# taking input of variable and list in same line
a, lst = int(input()), list(map(int, input().split()))

#finding the max value in list
max_value = max(lst)
# removing max value from list
while(max_value == max(lst)):
    lst.remove(max_value)
# printing second max value
print(max(lst))
