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

#Defining function to find maximim number in a given list
def myMax(my_list): 
    max = my_list[0] 
    for x in my_list: 
        if x > max : 
             max = x 
    return max
#Defining function to find minimum number in a given list
def myMin(my_list):
    min = my_list[0] 
    for x in my_list: 
        if x < min : 
             min = x 
    return min
print('Maximum: ', myMax(number_list))
print('Minimum: ', myMin(number_list))
