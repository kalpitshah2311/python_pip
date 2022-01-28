#20ce129 
#Kalpit Shah
# read the k and arr in single line
k,arr = int(input()),list(map(int, input().split()))
# convert the arr to set
myset = set(arr)
# the main logic
print(((sum(myset)*k)-(sum(arr)))//(k-1))
