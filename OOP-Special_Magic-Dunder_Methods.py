#Special Methods --> it's allow us to use some built-in operations in python, such as the Length function or the print function with our own user-created objects

#Lets see a simple example 
mylist = [1,2,3]

print(mylist)

len(mylist)

#What if i wanna check the Lenght of the object or maybe print it out
#Let's create a simple class
class Sample():
    pass

mysample = Sample()

#now if i check the length of my sample class it'll get a TypeError
len(mysample)

#or if i try to print out. it'll just gonna guve the location in my memory where this code is 
print(mysample)

#unlike my list, where if i tried to print it out. it'll actually get back mylist in a String form
print(mylist)

#so the question arises, how am i able to actually use build-in python function, such as Length or print with my own user-define object?
#this is where those special methods come into play

#Let's create a book class

class Book():
    #{__init__} was the first Spacial method we learned 
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

#Now let's imagine i want to print out my book
b = Book('Python rocks','Jose',200)

print(b)
#It just gonna say you have this book object in your memeory 

str(b)
#it gonna print the same Memory stuff in String formate

class Book():
    #{__init__} was the first Spacial method we learned 
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

#So to fix this we can use the Spacial method related to the string call, 
#Which is  __str__
    def __str__(self):
        return f"{self.title} by {self.author}"
        #I can return whatever i want to printed out. 

b = Book('Python rocks','Jose',200)

#now if i run i get back my sring
print(b)

class Book():
    #{__init__} was the first Spacial method we learned 
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author}"

    #We can also do the same with Length
    def __len__(self):
        return self.pages

b = Book('Python rocks','Jose',200)

print(b)

len(b)

#Let's say we wanna Delete the book object, we can do that with {del} keyword
#and let's say i wanna printout or report upon deleting the variable or you may want other things to occur when yopu delete the veriable

del b

print (b)

class Book():
    #{__init__} was the first Spacial method we learned 
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author}"

    #We can also do the same with Length
    def __len__(self):
        return self.pages

    #We can use __del__ spacial method
    def __del__(self):
        print("A book has been Deleted")

b = Book('Python rocks','Jose',200)

print(b)

len(b)

del b

print(b)








