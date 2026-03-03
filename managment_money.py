def expience():
    money_left=0

    while True:
        A=input("Enter input type credits / spent / exit:").lower()
        if A=="credits":
            while True:
                credits=float(input("Enter the credit: "))
                if credits==0:
                    break
                else:
                    money_left += credits
        elif A=="spent":
            while True:
                spent=float(input("Enter the Spent: "))
                if spent==0:
                    break
                else:
                    money_left -= spent
        elif A=="exit":
            break
        else:
            print("Enter valid input.")

    print(f"Total money left: {money_left}")
    
expience()
