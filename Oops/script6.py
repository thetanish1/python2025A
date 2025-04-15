# // Online Java Compiler
# // Use this editor to write, compile and run your Java code online

# class Main {
#     public static void main(String[] args) {
#         System.out.println("Try programiz.pro");
#         addition(12,4);
#         addition(12,4,4);
#         addition(12,4,4,5);
#     }
    
#     // polymorphism overloading 
#     public static addition(int x , int y){
#         System.out.println(x+y); 
#     }
#     public static addition(int x , int y ,int z){
#         System.out.println(x+y+z); 
#     }
#     public static addition(int x , int y ,int z , int a){
#         System.out.println(x+y+z+a); 
#     }
    
    
# }

# polymorphism ----> overloading ---> same class , same methodName , 
# different signature

class Calculator:

    # def addition(self,x,y):
    #     print(x+y)

    # def addition(self,x,y,z):
    # #     print(x+y+z)

    # def addition(self,x,y,z,a):
    #     print(x+y+z+a)

    def addition(self,a = None , b = None , c = None , d = None):
        if (a != None and b != None and c != None and d != None):
            print(a+b+c+d)
        elif(a != None and b != None and c != None):
            print(a+b+c)
        elif(a != None and b != None):
            print(a+b)
        else:
            print("incorrect input")



cal = Calculator()
cal.addition(12,4)
cal.addition(12,4,4)
cal.addition(12,4,4,5)


# overriding 
# same method , same signature but different class or has a relationship
class WorldBank:
    def loan(self):
        print("loan method called")
    def save(self):
        print("save method called")

class SBI(WorldBank):
    def loan(self):
        print("sbi loan method called")
    def save(self):
        print("sbi save method called")

sbiPune = SBI()
sbiPune.loan()
sbiPune.save()


# duck typing 
# operator overloading