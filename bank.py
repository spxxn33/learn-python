#input
username=input("Enter your username :")
password=input("Enter your password :")

#try using nested-if 
if username=="member" and password=="1234": #main if
    print("Welcome to system")
    service=input("select your service (1-2) : ")
    if service=="1": #secondary if
        print("Withdraw money")
    elif service=="2":
        print("Deposit money")
    else :
        print("Wrong service number")
else:
    print("Account not found")