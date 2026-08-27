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

#now let's create more attributes
class Dog():
    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots  #here we are expecting boolean True/False

my_dog = Dog(breed = 'Huskie', name = 'Sam', spots = False)

print(my_dog.breed, my_dog.name, my_dog.spots)
