# n=[1,2,3]
# for i in range (len(n)):
#     for j in  range(len(n)):
#         for t in range (len(n)):
#             print(i,j,t)

# n=10
# arr = [0] * n  # O(n) space
# for i in range(n):
#     print(i)

# n=3
# for i in range (n):
#     for j in range(n):
#      print('*',end='')
#     print()

# a=[1,2,3,4,5]
# b=[6,7,8,9,10]

# for x in a:
#     for y in b:
#      print(x+y)


# num = 10
# if num>0 or num>30 :
#     print('true')
# else:
#     print('false')

# num=10
# print("correct") if num>9 else print('incorrect') #terneary operator


# n=100
# print("Correct") if n>90 else print("incorrect")

# num=1
# while (num<=11):
#     print(num)
#     num+=1

# i1=1
# while(i1<200):
#     print(i1)
#     i1+=1
# a=100
# b=10
# print(a>b)

# for x in range(1,11):
#     print(x*2)

# i=1
# while(i<=10):
#     print(i*2)
#     i+=1

# for x in range(10,0,-1):
#     print(x)
dict = [
    {
        "fn": "t",
        "ln": "d"
    },
    {
        "tanish":"dewase",
        "dewase":"gygf"
    }
    ]
for x in dict:
    print(list(x)) #gives list 

for x in dict:
    print(x["fn"])