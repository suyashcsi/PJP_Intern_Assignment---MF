lower = int(input("Enter lower range between 10 and 99 :"))
upper = int(input("Enter upper range between 10 and 99 :"))

for num in range(lower,upper +1):
    if num > 1:
        for i in range(2,num):
            if(num % 2) == 0:
                break
        else:
            print(num)

