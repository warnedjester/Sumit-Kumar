#WAP to calculate the area of triangle:
from math import *
s1=int(input("Enter side one : "))
s2=int(input("Enter side two : "))
s3=int(input("Enter side three : "))
s=(s1+s2+s3)/2
area=sqrt(s*(s-s1)*(s-s2)*(s-s3))
print(area)