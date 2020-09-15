str='X-DSPAM-Confidence:0.8475'
count=0
fname=input("Enter the file name: ")
try:
    if fname=="na na boo boo":
        print("NA NA BOO BOO TO YOU-you have been punk'd!")
    else:
        fhand=open(fname)
        for line in fhand:
            if line.startswith('X-DSPAM-Confidence:'):
                count=count+1
        print('there were ',count,'subject lines in',fname)
except:
    print('file cannot be opened: ',fname)
    exit()