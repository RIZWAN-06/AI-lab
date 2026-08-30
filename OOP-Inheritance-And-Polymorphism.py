#Inheritance --> It's a way to form new classes using classesthat have already been defined.

#Let's create a simple base class, to understand it better
class Animal():
    def __init__(self):
        print ("Animal created")
#So we have a very simple Class here 

#If i create an instance of an Animal, it just gonna print out Animal created 
myanimal = Animal()
myanimal

#Now Let's crerate 2 more methods in our animal class
class Animal():
    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I'm an Animal")
    def eat(self):
        print("I'm eating")

myanimal = Animal()
myanimal.eat()
myanimal.who_am_i()


#Now Let's use this Animal class as our base class, so newly created class can use this base class in order to inherte some of it's methods

class Dog(Animal): #Before we never passed any argument but if pass in an Animal, I'm going to inherte from this class
    #I'm going to create an instance of the Animal class
    def __init__(self):
        Animal.__init__(self)


