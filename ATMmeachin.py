import random
def atm():
    balance=0
    while True:
        print("1.Create Account")
        print("2.Withdrawal Cash")
        print("3.Cash Deposit")
        print("4.Balance Enquiry")
        print("5.Exit")
        
        A=int(input())
        if A==1:
            print("Enter your details:")
            Account_name=input("Enter your name: ")
            age=int(input("Enter your age:"))
            id_proof=int(input("Enter your Id Number:"))
            number = random.randint(100000000000, 999999999999)
            print(number)
            create_pin=int(input("Create your four digit pin:"))
            balance=int(input("Enter your first balance:"))
        elif A==2:
                while True:
                    pin = int(input("Enter your PIN: "))
                    B=input(f"Exit / 1:").lower()
                    if B=="exit":
                        break
                    else:
                        if pin == create_pin:
                            amount=int(input("Enter amount:"))
                            if amount<=balance:
                                balance-=amount
                                print(f"Now your available balance:{balance} ")
                            else:
                                print("Unsuifficient balance in your accounte.")

                        else:
                            print("Incorrect PIN")
        elif A==3:
                while True:
                    pin = int(input("Enter your PIN: "))
                    B=input(f"Exit / 1: ").lower()
                    if B=="exit":
                         break
                    else:

                        if pin == create_pin:
                            amount=int(input("Enter amount:"))
                            balance+=amount
                            print(f"Now available balance in your account{balance}")
                        else:
                            print("Incorrect PIN")
        elif A==4:
                pin = int(input("Enter your PIN: "))

                if pin == create_pin:
                    print(f"your balance is {balance}")
                else:
                    print("Incorrect PIN")
        elif A==5:
             break
        else:
             print("Invalid option.")
atm()