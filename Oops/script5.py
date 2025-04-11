# # program 1 single inheritance
# class Father:
#     def __init__(self,fn,ln):
#         self.firstName = fn 
#         self.lastName = ln 

#     def displayName(self):
#         print(self.firstName + self.lastName)

# class Son(Father):
#     def __init__(self,fn,ln,sn):
#         super().__init__(fn,ln)
#         self.sname = sn

#     def displaySName(self):
#         print(self.sname + self.lastName)
        
# chinmay = Son("shirsh","deshpande","chinmay")
# print(chinmay.firstName)
# print(chinmay.lastName)
# print(chinmay.sname)
# chinmay.displayName()
# chinmay.displaySName()

# program 2
# multi-level

class GrandFather:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln 

    def displayName(self):
        print(self.firstName + self.lastName)

class Father(GrandFather):

    def __init__(self, fn, ln,ffn):
        super().__init__(fn, ln)
        self.fname = ffn

    def displayFName(self):
        print(self.fname + self.lastName)



class Son(Father):
    def __init__(self, fn, ln, ffn ,ssn):
        super().__init__(fn, ln, ffn)
        self.sname = ssn

    def displaySName(self):
        print(self.sname + self.lastName)


chinmay = Son("manohar","deshpande","shirish","chinmay")

print(chinmay.firstName)
print(chinmay.lastName)
print(chinmay.sname)
print(chinmay.fname)

chinmay.displayFName()
chinmay.displaySName()
chinmay.displayName()


# heriarchical inhertiance
# class Mother:
#     def __init__(self,fn,ln):
#         self.firstName = fn 
#         self.lastName = ln 

#     def displayMname(self):
#         print(self.firstName + self.lastName)

# class Son(Mother):
#     def __init__(self, fn, ln,ssn):
#         super().__init__(fn, ln)
#         self.sname  = ssn
#     def displaySon(self):
#         print(self.firstName + self.lastName)


# class Daughter(Mother):
#     def __init__(self, fn, ln,ddn):
#         super().__init__(fn, ln)
#         self.dname  = ddn
#     def displayDaughter(self):
#         print(self.firstName + self.lastName)


# chinmay  = Son("kanchan","deshpande","chinmay")
# gauri = Daughter("kanchan","deshpande","gauri")

# chinmay.displayMname()
# chinmay.displaySon()

# gauri.displayMname()
# gauri.displayDaughter()



# multiple inheritance 



class Father:
    def __init__(self,fn,ln):
        print("father constructor called")
        self.fname = fn 
        self.lname = ln

    def displayFName(self):
        print(self.fname + self.lname)

class Mother:
    def __init__(self,fn,ln):
        print("mother constructor called .....")
        self.mname = fn 
        self.lname = ln

    def displayMName(self):
        print(self.mname + self.lname)

class Son(Mother,Father):
    def __init__(self, fn, ln,ssn):
        super().__init__(fn, ln)
        self.sname = ssn

    def displaySname(self):
        print(self.sname + self.lname)


chinmay = Son("kanchan","deshpande","chinmay")







