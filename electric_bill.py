def electric_bill():
    unit=int(input("Enter electric unit: "))

    if unit <=100:
        bill=unit * 5
    elif unit<=300:
        bill =unit *7
    else:
        bill = unit *10
    
    print(f"Electric bill : {bill}.")

electric_bill()