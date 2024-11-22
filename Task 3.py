num=int(input("Type in a number from 1 to 10"))
while num<0 or num>10:
    print("Number out of range")
    num=int(input("Type in a number from 1 to 10"))
    count=0
if num%2==0: