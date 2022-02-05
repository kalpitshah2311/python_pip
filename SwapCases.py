
#20ce129 Kalpit shah pracical 5

def swap_case(s):
    case_change=[]
    for i in range(len(s)):
        if (s[i].isupper())==True:
            case_change.append(s[i].lower())
        elif (s[i].islower()==True):
            case_change.append(s[i].upper())
        else:
            case_change.append(s[i])    
        stri=''
    return stri.join(case_change)


    if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
