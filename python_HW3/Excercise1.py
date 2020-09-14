#========Excercise1/chapter5====================
count = 0
total = 0
avg = 0
choice = True
while choice:
  number = input ('Enter a number: ')
  try:
     number = float(number)
     count = count + 1 
     total = total + number
     avg = total / count
  except:
    if number.lower()=='done':
      break
    else:
      print ('Invalid Input')
      continue
print (f'total:{total} \ncount: {count}\naverage:{avg}')