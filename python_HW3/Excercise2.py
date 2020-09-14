# Exercise2/Chapter5
number_list=[]
choice = True
while choice:
    number = input ('Enter a number: ')
    if number.lower()=='done':
      break
    try:
        number = int(number)
    except ValueError:
        print('Invalid input')
    number_list.append(number)

print('Maximum: ', max(number_list))
print('Minimum: ', min(number_list))
