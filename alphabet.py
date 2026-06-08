alphabet=input("Enter the alphabet:")
if alphabet in "AEIOUaeiou":
    print("The alphabet is a vowel.")
elif alphabet in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
    print("The alphabet is a consonant.")
else:
    print("Invalid input.")

