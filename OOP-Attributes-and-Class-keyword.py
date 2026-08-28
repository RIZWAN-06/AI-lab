#lets explore how we can use "class_keyword" to create user define object

#class name is capatalis for the class we follow (camel casing for every word that it follows

class Sample():
  pass 

my_sample = Sample()

print(type(my_sample))

#Now let's create attributes
class Dog():
    def __init__(self,breed):
        self.breed = breed

my_dog = Dog(breed = 'Lab')
print(my_dog.breed) #we can leter add more attributes

#if that self. feel hard to understand let's make it Simple 

class Dog():
    def __init__(self,dogBreed):
        self.MyAttribute = dogBreed

my_dog = Dog(dogBreed = 'Huskie')
print(my_dog.MyAttribute)

#now let's create more attributes/And Class Object attributes
class Dog():

    #Class object attributes
    #Same for any instance of a Class
    species = 'Mammal'

    def __init__(self,breed,name,spots):
        #attributes
        #we take in the arguments
        #assign it to self.attributes_name
        self.breed = breed
        self.name = name
        self.spots = spots  #here we are expecting boolean True/False
    
    #Operations/Action ---> Methods
    
    def bark(self,number): #Methos can take other arguments too 
        print('WOOF! My name is {} and the number is {}'.format(self.name,number))  
        #So notice here we are no longer saying {self} because number is already gonna be provided by the user 



#now let's create the instance
my_dog = Dog(breed = 'Huskie', name = 'Sam', spots = False)

print(my_dog.breed, my_dog.name, my_dog.spots, my_dog.species)
print(my_dog.species)
print(my_dog.bark(20))




#NOW LETS CREATE A NEW CLASS FOR CLEARENCE EVERYTHING

#Let's create a class called Circle
class Circle():
    #class object attribute 
    pi = 3.14  #so regardless of instance of a Circle i make i'll always beable to referance Pi here as 3.14

    def __init__(self,radius = 1): #seting radious default value 
        self.radius = radius
        #attribute doesn't necessary have to be define from a particular call
        self.area = radius*radius*self.pi   #Since Pi is a class object attribute we can simply call it by the name of the class


    #now lets make a method here 
    def get_circumference(self):
        return self.radius*Circle.pi*2


#Let's create the instance
my_circle = Circle(30)  #We can provide value for radious

#Let's call it 

print(my_circle.pi)
print(my_circle.radius) 

#now let's see how the Method is working
print(my_circle.get_circumference())

#Let's call the area 
print(my_circle.area)
