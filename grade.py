score=input("Enter your score")
score=int(score)
if score<=100 and score>=80:
    print("Your grade is A.")
elif score<=79 and score>=70:
    print("Your grade is B.") 
elif score<=69 and score>=0:
    print("Your grade is C.")
else:
    print("Invalid input.")