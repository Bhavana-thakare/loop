print("Enter a Character: ", end="")
ch = input()
chlen = len(ch)
if chlen==1:
    asc = ord(ch)
    print("ASCII Value of " +(ch)+ " = " +str(asc))
else:
    print("Invalid Input!")