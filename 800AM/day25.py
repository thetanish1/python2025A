# // Online Java Compiler
# // Use this editor to write, compile and run your Java code online

# class Main {
#     public static void main(String[] args) {
#         System.out.println("Try programiz.pro");
#         addition(12,4);
#         addition(12,4,5);
#         addition(12,4,5,6);
#     }
    
#     public static void addition(int x , int y){
#          System.out.println(x+y);
#     }
#     public  static void addition(int x,int y,int z){
#          System.out.println(x+y+z);
#     }
#     public static void addition(int x,int y,int z,int a){
#          System.out.println(x+y+z+a);
#     }
    
# }


class Calculator:

    # def addition(self,a,b):
    #     print(a+b)
    
    # def addition(self,a,b,c):
    #     print(a+b+c)

    # def addition(self,a,b,c,d):
    #     print(a+b+c+d)

    def addition(self ,a = None , b = None , c = None , d = None):
        if a != None and b != None and c != None and d != None:
            print(a+b+c+d)
        elif a != None and b != None and c != None:
            print(a+b+c)
        elif a != None and b != None:
            print(a+b) 
        else :
            print("please provide correct input")       

calC = Calculator()
calC.addition(12,3)
calC.addition(12,3,5)
calC.addition(12,3,5,5)