#basic calculator
print("menu")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.divison")
option=int(input("enter the option"))
num1=int(input("enter the number 1:"))
num2=int(input("enter the number 2:"))
if(option==1):
    sum=num1+num2
    print(sum)
elif(option==2):
    sub=num1-num2
    print(sub)
elif(option==3):
    mul=num1*num2
    print(mul)
elif(option==4):
    div=num1/num2
    print(div)
else:
    print("invalid option")