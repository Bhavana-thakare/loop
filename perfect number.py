n=int(input("Enter the number:"))
a=0
b=1
while b<n:
    if n%b==0:
        a=a+b
    b+=1
if b==n:
    print("perfect number")
else:
    print("Not perfect number")