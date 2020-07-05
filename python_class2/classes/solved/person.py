#Create a class named Person, use the __init__() function to assign values for name and age
#The __init__() function is called automatically every time the class is being used to create a new object
#All classes have a function called __init__(), which is always executed when the class is being initiated
#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
# create object of class person
p1=Person("max",25)
print(p1.name)
print(p1.age)