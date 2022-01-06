a=1
b=0
while a<=11:
    weight=int(input("Enter the weight:"))
    b=b+weight
    average=b/a
    a+=1
print(b,average)
if average%5==0:
    print("Divisible")
else:
    print("Not divisible")