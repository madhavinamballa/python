#=============break statement=============
num=int(input("Enter a number: "))
for x in range(2,num):
    if num%x==0:
        print("{} is not prime".format(num))
        break
    else:
        print ("{} is prime".format(num))
#===============continue statement==============
#================else statements=========

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")