from collections import Counter
fname=input("Enter the file name: ")
count=0
values=[]
fhand=open(fname)
for line in fhand:
#         line=line.strip()
    if not line.startswith('From'):
        continue
    count=count+1
    words=line.split()
    values.append[words[1]]
list_dict=dict(Counter(values))
print(list_dict)
def keywithmaxval(d):
     v=list(d.values())
     k=list(d.keys())
     return [k[v.index(max(v))],max(v)]
print(keywithmaxval(list_dict)[0],keywithmaxval(list_dict)[1])

def keywithminval(d):
     v=list(d.values())
     k=list(d.keys())
     return [k[v.index(min(v))],min(v)]
print(keywithmaxval(list_dict)[0],keywithmaxval(list_dict)[1])
print(keywithminval(list_dict)[0],keywithminval(list_dict)[1])