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
    my_list.append(words[1])
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

# Enter the file name: mbox-short.txt
# cwen@iupui.edu 10
# wagnermr@iupui.edu 2




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
    my_list.append(words[1])
domain_names=[]
for i in domain_names:
    lim.append(i.split("@")[1])
list_lim=dict(Counter(lim))
print(list_lim)



# Enter the file name: mbox-short.txt
# {'uct.ac.za': 12, 'media.berkeley.edu': 8, 'umich.edu': 14, 'iupui.edu': 16, 'caret.cam.ac.uk': 2, 'gmail.com': 2}