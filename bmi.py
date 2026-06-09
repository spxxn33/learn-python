#input
w=input ("Enter your weight(Kg) :")
h=input ("Enter your height(M) :")
BMI=float(w) / (float(h) ** 2)
bmi=None

#process
if BMI<18.5 and BMI>=0:
    bmi="Underweight"
elif BMI>=18.5 and BMI<25:
    bmi="Normal weight"
elif BMI>=25 and BMI<30:
    bmi="Overweight"
else:
    bmi="Obesity"

#output
print("Your BMI is ",BMI)
print("Category: ",bmi)