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
        print("Dog created")



mydog = Dog()

#now all those old methods that were available for Animal, are now available for mydog
mydog.eat()


#We can also overwrite order methods

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    #overwrite Method 
    def who_am_i(self):
        print('I Am A Dog!')

#Let's run this 

mydog = Dog()
mydog.eat()
mydog.who_am_i()

#you are also able to add new methods
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
 
    def who_am_i(self):
        print('I Am A Dog!')
    
    #new methods
    def bark(self):
        print("WOOF!")


#let's run this
mydog = Dog()
mydog.bark()



#POLYMORPHISM ---> In python POLYMORPHISM refer to the way in which different object classes can share the same methods and then those methods can be called from the same place, even tho varity of different objects might be passed in. 


