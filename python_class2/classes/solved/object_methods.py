class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #insert a function that prints hello 
    def hellofunc(self):
        #The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class
        #It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class
        print("hello my name is "+self.name)

# create object of class person
p1=Person("max",25)
#execute function on object p1
p1.hellofunc()