s1 = 'Hi, Welcome to Wipro'
count1 = 0
count2 = 0
for i in s1:
    if(i.islower()):
        count1 = count1 +1
    elif(i.isupper()):
        count2 = count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)
