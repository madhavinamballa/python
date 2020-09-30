from collections import Counter
fname=input("Enter the file name: ")
count=0
my_list=[]
fhand=open(fname)
for line in fhand:
#         line=line.strip()
    if not line.startswith('From'):
        continue
    count=count+1
    words=line.split()
    my_list.append[words[1]]
my_list=dict(Counter(my_list))

def keywithmaxval(d):
     v=list(d.values())
     k=list(d.keys())
     return [k[v.index(max(v))],max(v)]


def keywithminval(d):
     v=list(d.values())
     k=list(d.keys())
     return [k[v.index(min(v))],min(v)]
print(keywithmaxval(my_list)[0],keywithmaxval(my_list)[1])
print(keywithminval(my_list)[0],keywithminval(my_list)[1])
