#input and match-case statement
#input
service=int(input("Enter a service number (1-3) : "))

#process
match service:
    case 1:
        print("Withdraw money")
    case 2:
        print("Deposit money")
    case 3:
        print("Check balance")
    case _ :
        print("Wrong service number")