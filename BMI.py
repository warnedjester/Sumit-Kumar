height=float(input("enter the height in meters"))
weight=float(input("enter the weight in kgs"))
BMI=weight/height*height
if(BMI<18.5):
    print("underweight")
elif(BMI>=18.5 and BMI<=24.9):
    print("normal")
elif(BMI>=25.0 and BMI<=29.9):
    print("overweight")
elif(BMI>30.0):
    print("obese")
else:
    print("invalid output")