i=int(input("Enter the number:"))
a=i
sum=0
while i>0:
   sum=sum+(i%10)*(i%10)*(i%10)
   i=i//10
if a==sum:
   print(a,"is armstrong number")
else:
   print(a,"is not armstrong number")




# 0,1,153,370,371,407




   

