num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
op=input("enter the operation to be done")
if(op=='+'):
    sum=num1+num2
    print(sum)
elif(op=='-'):
    sub=num1-num2
    print(sub)
elif(op=='//'):
    div=num1//num2
    print(div)
elif(op=='*'):
    mul=num1*num2
    print(mul)
else:
    print("invalid operator")