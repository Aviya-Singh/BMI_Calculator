#Take input value from the user 
weight=float(input("Enter your weight(in kgs):"))
height=float(input("Enter your height(in m)"))

#Calculate BMI 
bmi=weight/(height**2)

#Round BMI to 2 decimals
bmi=round(bmi,1)
#print(bmi)

#Conditional statements
if bmi < 18.0:
    idealWeight=round(18.0*(height**2),1)
    print(f"Your BMI is {bmi}. You are Under Weight. You should atleast reach {idealWeight} to become healthy.")

elif bmi > 18.0 and bmi < 24.9:
    print(f"Your BMI is {bmi}. You are Normal Weight.")

elif bmi > 25.0 and bmi < 29.9:
    idealWeight=round(24.9*(height**2),1)
    print(f"Your BMI is {bmi}. You are Over Weight. You should atleast reach {idealWeight} to become healthy.")

else:
    idealWeight=round(24.9*(height**2),1)
    print(f"Your BMI is {bmi}. You are Obese. You should atleast reach {idealWeight} to become healthy.")