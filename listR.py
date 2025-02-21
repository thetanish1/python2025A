i2 = 1
while(i2 <= 5):
    print(i2) # 1 #2 #3
    if i2 == 3:
        break
    i2 = i2 + 1 #2 #3

# continue statement with while loop

i3 = 1
while (i3 <= 5):
    if i3 == 3:
        i3 = i3 + 1
        continue
    print(i3) #1 #2
    i3 = i3 + 1 #2 #3