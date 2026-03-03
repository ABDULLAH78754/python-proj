def grocery_bill():
    total = 0

    while True:
        price = float(input("Enter the price (0 to stop): "))
        
        if price == 0:
            break
        elif price > 0:
            total += price
        elif price < 0:
            total += price
        else:
            print("Enter valid positive price.")

    print(f"The total bill amount is: {total}")

grocery_bill()