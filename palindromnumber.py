number=int(input("Enter any number :"))
a=number
b=0
while(number>0):
    digit=number%10
    b=b*10+digit
    number=number//10
if(a==b):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")

