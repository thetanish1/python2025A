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
# dictt = [
#     {
#         "fn": "t",
#         "ln": "d"
#     },
#     {
#         "fn":"dewase",
#         "dewase":"gygf"
#     },
#     {
#         "fn":"sdf",
#         "sdf":"rr"
#     }
#     ]
# for x in dictt:
#     print(list(x)) #gives list 

# for x in dictt:
#     print(x['fn'])



tanish=['sarika','disha','palak','mahi','vanshika']

i=0
while(i<len(tanish)):
    print(i)
    i+=1
# for x in tanish:
#     print(x[0])

print(len(tanish))

tanish[0]='rishika'
print(tanish)

print('rishika' in tanish)
print('disha'in tanish)
print('tanish' in tanish)

print(len(tanish))


numbers=[1,2,3,4,5,6,7]
print(max(numbers))
print(min(numbers))
del numbers

# ..........................................................................................

names=['tanish','disha','palak','rishika','vanshika']
names.append('mahi') #add in last
print(names)

names.pop() #last delete
print(names)

names.sort() #alpabetic order
print(names)

names.reverse() #last el in first el
print(names)

names.remove('tanish') #specific value delete
print(names)

r=names.count('disha') #count element in list
print(r)


names=['tanish','disha','palak','rishika','vanshika']
name1=['shyam','krishna','mohan','kanha']
names.extend(name1) #first mein second ki value jayengi
print(names)
print(name1)

name1.sort()
print(name1)


vehicle={
    #property:value
    #key: value
    "color":"red",
    "type":"Mercedes",
    "company":"mercedes",
    "color":"red",
}

print(vehicle)
print(len(vehicle))

for x in vehicle:
    print(x,vehicle[x])

for x in vehicle.keys():
    print(x)

for x in vehicle.values():
    print(x)

for x in vehicle.items():
    print(x)
    print(type(x))











