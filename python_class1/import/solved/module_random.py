#Python - Random Module
#Functions in the random module depend on a pseudo-random number generator function random(), 
#which generates a random float number between 0.0 and 1.0.
#This number is used to generate a float random number less than 1 and greater or equal to 0.
import random
print(random.random())
#random.randint()
#Returns a random integer between the specified integers.
print(random.randint(0,9))
#random.choice()
#Returns a randomly selected element from a non-empty sequence.
print(random.choice("madhavi"))
print(random.choice([12,23,45,67,65,43]))
# random.shuffle()
#This functions randomly reorders the elements in a list
numbers=[12,23,45,67,65,43]
random.shuffle(numbers)
print(numbers)