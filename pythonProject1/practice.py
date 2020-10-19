def palindrom(num):
    if num<0:
        return Flase
    rev=0
    original=num
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    if rev==original:
        return True
    else:
        return False
print(palindrom(121))

#=========================

def revstring(s):
    s=list(s.split(" "))
    print(s)
    j=-1
    middle=len(s)//2
    tmp=""
    for i in range(middle):
        tmp=s[i]
        s[i]=s[j]
        s[j]=tmp
        j-=1
    return s
print(revstring("madhavi"))