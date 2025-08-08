
class  Person:
    fn = None
    ln = None

    def displayName(self):
        print(self.fn + self.ln)


chinmay  = Person()
print(chinmay.fn)
print(chinmay.ln)
chinmay.fn  = "chinmay"
chinmay.ln = "deshpande"
chinmay.displayName()

amol = Person()
print(amol.fn)
print(amol.ln)
#amol.displayName()
amol.fn = 'amol'
amol.ln = 'rao'
amol.displayName()
print(amol.fn)
print(amol.ln)

# class Person:
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln 

#     def displayName(self):
#         print(self.firstName + self.lastName)

# sarika = Person("sarika","pansare")
# sarika.displayName()

# amol = Person("amol","rao")
# amol.displayName()
