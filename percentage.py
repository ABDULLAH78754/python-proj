a=input("Enter outcome percentage / actual /total:").lower()
if a=="percentage":
    total=float(input("Enter total value: "))
    actual=float(input("Enter actual value: "))
    result=(actual/total)*100
    print(f"Percentage value is {result}%.")

elif a=="actual":
    total=float(input("Enter total value: "))
    percentage=float(input("Enter Percentage value: "))
    result=(percentage*total)/100
    result=round(result)
    print(f"Actual value is {result}.")

elif a=="total":
    actual=float(input("Enter actual value: "))
    percentage=float(input("Enter Percentage value: "))
    result=(actual/100)*percentage
    result=round(result)
    print(f"Total value is {result }.")

else:
    print("Please enter valide input.")
    