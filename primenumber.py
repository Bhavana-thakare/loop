i=int(input("enter the number:"))
a=1
# b=0
while a<=i:
    if i%a==0:
        b=b+1
    a=a+1
if b==2:
    print("prime")
else:
    print("compositive number")
