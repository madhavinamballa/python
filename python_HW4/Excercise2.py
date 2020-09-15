# Excercise2/Chapter7
str='X-DSPAM-Confidence:0.8475'
fname=input("Enter the file name: ")
try:
    fhand=open(fname)
except:
    print('file cannot be opened: ',fname)
    exit()
count=0
total=0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count=count+1
#         print(line)
        start = line.find(':')
        end = len(str)
        number = str[start+1:end]
        fpnumber = float(number)
        total=total+fpnumber
print('there were ',count,'subject lines in',fname)
print('Average Spam Confidence: ',total/count)