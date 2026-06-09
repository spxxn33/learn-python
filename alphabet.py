#input
alphabet=input("Enter the alphabet :")
print("Your alphabet is : ",alphabet)
apbet=None

#process
if alphabet in "AEIOUaeiou":
    apbet="The alphabet is a vowel."
elif alphabet in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
    apbet="The alphabet is a consonant."
else:
    apbet="Invalid input."

#output
print(apbet)
