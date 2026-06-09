#input
score=int(input("Enter your score : "))
print("Your score is :",score)
grade=None

#process
if score<=100 and score>=80:
    grade="A"
elif score<=79 and score>=70:
    grade="B"
elif score<=69 and score>=0:
    grade="C"
else:
    print("N (Invalid)")

#output
print("Your grade is ",grade)

