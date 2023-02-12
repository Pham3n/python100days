# BMi Calculator calculates a person's body mass index by dividing their weight by height squared

from decimal import Rounded


height = float(input("Give me your height in metres:"))
weight = float(input("Now give me your weight in kilograms:"))

bmi = weight/height**2

print(f"Your BMI is {bmi}")
rbmi = round(bmi)
print(f"Your rounded BMI is {rbmi}")

#Round results into whole number
#Underweight <18.5, 18.5 < 25 Normal weight, 25 =<30 Overweight, 30 < 35 Obese, < 35 Clinicaly obese

if bmi < 18.5 : print(f"Your BMI is {rbmi}, you are underweight")
elif bmi < 25 : print(f"Your BMI is {rbmi}, you are normal weight")
elif bmi < 30 : print(f"Your BMI is {rbmi}, you are overweight")
elif bmi < 35 : print(f"Your BMI is {rbmi}, you are obese")
else  : print(f"Your BMI is {rbmi}, you are clinicaly obese")