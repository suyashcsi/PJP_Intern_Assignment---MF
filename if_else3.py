a = int(input("Enter a Number1 : "))
b = int(input("Enter a Number2 : "))

lastdigit1 = a%10
lastdigit2 = b%10

if(lastdigit2 == lastdigit1):
    print("true")
else:
    print("False")
