fn = 'chinmay'
print(fn)

fn = "chinmay"
print(fn)

info = """
I am learning js and python for automation
and this is imp
"""
info2 = '''
I am learning js and python for automation
and this is imp
'''
print(type(fn))

# program 2
city = "pune"
print(city)
h = len(city)
print(h)

# program 3
city = "nagpur"
e = city[0]
print(e)

#program 4
# mutables ??
# city2 = "mumbai"
# city2[0] = "y"

#program 5
city = "pune"
# 0   1   2   3
# p   u   n   e 
print(city[0])
print("p" in city)
print("pu" in city)
print("P" in city)

#program 6
fn = "arna"
print(fn)

# program 7
city = "pune"
#  0    1   2   3
#  p    u   n   e

for c in range(len(city)):
    print(c)
    print(city[c])

for char in city:
    print(char)

k = 0
while(k < len(city)):
   # print(k)
    print(city[k])
    k = k + 1

# program 6

city2 = "chandrapur"

# 0   1   2   3   4   5   6  7  8  9
# c   h   a   n   d   r   a  p  u  r
#-10 -9  -8  -7  -6  -5  -4 -3 -2 -1

#slicing (startIndex:endIndex(not inclueded):step)
# len - 1 is always index

# print(city2[:6])
# print(city2[0:10])
# print(city2[1:6])
# print(city2[2:-1])
# print(city2[-8:8])
# print(city2[-1:-3])
print(city2[::2])
print(city2[::-1])


# my first name is chinmay and lastName is deshpande
fn = "chinmay"
ln = "deshpande"

print("My firstName is "+fn+" and my lastName is "+ln)
print(f"My firstName is {fn} and my lastName is "+ln)




