# write a function  that returns the arithmetic average fora list of numbers
def average(numbers):
    length=len(numbers)
    total=0.0
    for number in numbers:
        total+=number
    return total/length

# Test your function 
print(average([1,5,8]))
print(average([10,20,30]))