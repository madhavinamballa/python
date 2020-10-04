#Excercise2 Chapter 10
from collections import Counter
fname=input("Enter the file name: ")
count=0
my_list=[]
fhand=open(fname)
for line in fhand:
#         line=line.strip()
    if not line.startswith('From'):
        continue
#     count=count+1
    words=line.split()
    if len(words)==7:
#         print(words)
        my_list.append(int(words[-2].split(":")[0]))
 
my_list=dict(Counter(my_list))
sorted(my_list.keys())
for key in sorted(my_list.keys()) :
    print(key , my_list[key])


# Enter the file name: mbox-short.txt
# 4 3
# 6 1
# 7 1
# 9 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1
# ========================================
#Excercise2 Chapter 10
import string

counts = 0                          # Initialize variables
dictionary_counts = dict()
relative_lst = list()

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()

    # Removes numbers and punctuation then sets all letters to lower case
    words = line.split()
    for word in words:
        for letter in word:
            # Count each letter for relative frequencies
            counts += 1
            if letter not in dictionary_counts:
                dictionary_counts[letter] = 1
            else:
                dictionary_counts[letter] += 1

for key, val in list(dictionary_counts.items()):
    relative_lst.append((val / counts, key))  # Computes the relative frequency

relative_lst.sort(reverse=True)         # Sorts from highest rel freq

for key, val in relative_lst:
    print(key, val)

# Enter file name: mbox-short.txt
# 0.09290243193820177 e
# 0.08926221523422145 a
# 0.07680344538820433 i
# 0.0713345752226001 o
# 0.06945465110317366 r
# 0.06921538803342847 t
# 0.06388323962196435 s
# 0.05337275477244373 u
# 0.052774597098080765 c
# 0.04400731461384649 n
# 0.04267427751098046 p
# 0.04163177413566216 m
# 0.03424879941209646 d
# 0.03130928169808419 l
# 0.023789585220378377 h
# 0.021482405619264094 f
# 0.019944285885187908 k
# 0.01938030864935997 b
# 0.01755165518773606 g
# 0.017038948609710662 v
# 0.01638952027754516 j
# 0.01098901098901099 y
# 0.010014868490762736 w
# 0.008237485686941364 x
# 0.0013330371028660297 z
# 0.0009741424982482526 q

# ==========================================
#Excercise1 Chapter 11

import re
# regexp = input('Enter a regular expression: ')
x=input('Enter a regular expression.')
file_name='mbox-short.txt'
file = open('mbox-short.txt')

count = 0
for line in file:
  line=line.rstrip()
  if re.search('\\b' + x + '\\b', line):
    count=count+1
print (f'{file_name} had {count} lines that matched {x}')

# Enter a regular expression.^Author
# mbox-short.txt had 27 lines that matched ^Author

# Enter a regular expression.^X-
# mbox-short.txt had 216 lines that matched ^X-

# Enter a regular expression.java$
# mbox-short.txt had 60 lines that matched java$

# =============================================
#Excercise2 Chapter 11
import re
count = 0
revisions = 0
x=input('Enter file:')
#Opening the file so that we can search through it
hand = open(x)
for line in hand:
    line = line.rstrip()
    if re.findall('New Revision: 397*', line):
      rev_num = line[14:19]
      count += 1
      revisions = revisions + float(rev_num)
#Using our count and sum from before, we can not calculate the average      
average = revisions/count
print(int(average))

# Enter file:mbox-short.txt
# 39756