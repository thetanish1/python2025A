

# list , dictionary ,set , tuple ,string 
# names = ["chinmay","shirsh","ram"]
# numbers = [11,22,33,4]
# info = {
#     "fn":"chinmay",
#     "ln":"deshpande"
# }

# user defined 
# class 

# program 1

# class Person:
#     firstName = None
#     lastName = None

#     def displayName(self):
#         print(self.firstName + self.lastName)


# amol = Person()
# amol.firstName = "amol R"
# amol.lastName = "Rao"
# # print(amol.firstName)
# # print(amol.lastName)
# # amol.displayName()
# amol.displayName()

# chinmay = Person()
# print(chinmay.firstName)
# print(chinmay.lastName)
# chinmay.firstName ="chinmay"
# chinmay.lastName = "deshpabnde"
# chinmay.displayName()


# program 2

class Person:

    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln
    
    def displaName(self):
        print(self.firstName + self.lastName)

amol2 = Person("amol","rao")
amol2.displaName()

chinmay2 = Person("chinmay","deshpande")
print(chinmay2.firstName)
print(chinmay2.lastName)
chinmay2.displaName()




