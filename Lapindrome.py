# 20ce129 Kalpit Shah Practical 7 Lapindrome

num = int(input())
s1 = ""
s2 = ""
for i in range(num):
    s =input()
    l = len(s)
    mid = int(l / 2)
    if(l%2==0):
        s1 = s[:mid]
        s2 = s[mid:]
    else:
        s1 = s[:mid]
        s2 = s[mid+1:]
    l1 = list(s1)
    l2 = list(s2)
    l1.sort()
    l2.sort()

    if(l1==l2):
        print("YES")
    else:
        print("NO")
