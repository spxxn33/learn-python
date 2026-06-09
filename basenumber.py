#input
from unicodedata import digit
    
number = inpt("Enter a number(0-4095) : ")
print("Your number is : ", number)

#process
if number<=4095 and number>=0:
    digit in number:
    is_base8 = True
    if digit not in "01234567":
        is_base8 = False
        break
else:
    print("Invalid input. Please enter a number between 0 and 4095.")
#output
if is_base8 and len(number) > 0:
    print("base 8 number")
else:
    print("not base 8 number")