from collections import Counter
fname=input("Enter the file name: ")
count=0
email=[]
try:
    fhand=open(fname)
    for line in fhand:
#         line=line.strip()
        if not line.startswith('From'):
            continue
        count=count+1
        words=line.split()
        email.append[words[1]]
        print(words[1])
    print('there were ',count,'lines in the file with From as the first word')
except:
    print('file cannot be opened: ',fname)
    exit()
list_dict=dict(Counter(email))
print(list_dict)
for key,value in list_dict.items():
    print(key,': ',value)
sort_orders = sorted(list_dict.items(), key=lambda x: x[1], reverse=True)

for i in sort_orders:
    print(i[0], i[1])
