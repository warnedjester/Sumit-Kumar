p=int(input("Enter principle :"))
t=int(input("Enter time taken :"))
n=int(input("No.of time interest applied per year :"))
r=float(input("Enter rate :"))
ci=p*((1+r/n)**(n*t))-p
print("compound interest = ",ci)