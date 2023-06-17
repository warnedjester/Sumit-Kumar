num=int(input("enter the number"))
fact = 1
if(num<1):
    print("factorial doesnt exist")
elif(num==0):
    print("factorial is 1")
else:
for i in range(1, num+1):
	fact = fact * i
print(fact)
