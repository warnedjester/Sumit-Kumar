num1=int(input())
num2=int(input())
num3=int(input())
if(num1>num2):
    if(num2<num3):
        print("num1 is largest")
elif(num2>num3):
    if(num3<num1):
        print("num2 is largest")
else:
    print("num3 is the largest")