w=input ("Enter your weight :")
h=input ("Enter your height :")
BMI=float(w) / (float(h) ** 2)
print("Your BMI is ",BMI)
if BMI<18.5:
    print("Underweight")
elif BMI>=18.5 and BMI<25:
    print("Normal weight")
elif BMI>=25 and BMI<30:
    print("Overweight")
else:
    print("Obesity")