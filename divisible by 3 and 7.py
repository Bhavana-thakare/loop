a=1
while a<=100:
    if a%3==0 and a%7==0:
        print("Navgurukul")
    elif a%7==0:
        print("Gurukul")
    elif a%3==0:
        print("nav")
    else:
        print(a)
    a+=1