#WAP prime number or not
num=int(input("enter the number"))
if num>1:
     for i in range(2,num):
         if(num%i==0):
              print(" not prime number")
              break
     else:
        print("prime number")
        
        
    