#Excercise5/chapter8
fname=input("Enter the file name: ")
count=0
try:
    fhand=open(fname)
    for line in fhand:
#         line=line.strip()
        if not line.startswith('From'):
            continue
        count=count+1
        words=line.split()
        print(words[1])
    print('there were ',count,'lines in the file with From as the first word')
except:
    print('file cannot be opened: ',fname)
    exit()