#WAP to input a number and print the sum of its digit
num=int(input("enter the number"))
s=0
while(num!=0):
    rem=num%10
    s=s+rem
    num=num//10
print(s)