num=int(input("Enter the number:"))
a=num
sum=0
while a>0:
    b=a%10
    sum=sum+b
    a=a//10
a+=1
if num%sum==0:
    print(num,"is a harshad number ")
else:
    print(num,"is not a harshad number")



