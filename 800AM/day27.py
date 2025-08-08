

# Ducking typing
# class Duck:
#     def talk(self):
#         print("Quack Quack")

# class Human:
#     def talk(self):
#         print("Hello hi")

# class Dog:
#     def bark(self):
#         print("Bow Bow")

# class Cat:
#     def CatSound(self):
#         print("meow meow")


# a  = Duck()
# b =  Human()
# c =  Dog()
# d = Cat()


# def call_talk(obj):
#     if hasattr(obj,'talk'):
#         obj.talk()
#     elif hasattr(obj,'bark'):
#         obj.bark()
#     elif hasattr(obj,'CatSound'):
#         obj.CatSound()

# call_talk(a)
# call_talk(b)
# call_talk(c)
# call_talk(d)

# program 2

# operator overloading - + 

print(1 + 1)
print("hello"+ "world")


class Bookx:
    def __init__(self,pages):
        self.pages = pages


class Booky:
    def __init__(self,pages):
        self.pages = pages
    
    def __add__(self,other):
        return self.pages + other.pages
    
    def __gt__(self,other):
        return self.pages > other.pages

mahabharat = Bookx(250)
ramayan = Booky(200)

#print(mahabharat+ramayan)
print(ramayan+mahabharat)
print(ramayan > mahabharat)
print(ramayan.pages > mahabharat.pages)

#print(mahabharat.pages + ramayan.pages)
