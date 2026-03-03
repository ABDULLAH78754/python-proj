#N1 = float(input("Enter first number: "))
#operator = input("Enter an operator (+ - * /): ")
#N2 = float(input("Enter Second number: "))
#if operator =="+":
 #   print(N1 + N2)
#elif operator =="-":
 #   print(N1 - N2)
#elif operator =="*":
 #   print(N1 * N2)
#elif operator =="/":
 #   print(N1 / N2)
#else:
 #   print("Please enter valid operator.")

def calculator():
    print("Simple Calculator (Enter 0 to stop)")
    
    result = None   # Initially no result
    
    while True:
        try:
            value = float(input("Enter number (0 to stop): "))
            
            if value == 0:
                break

            # First number automatically becomes result
            if result is None:
                result = value
                continue

            operator = input("Enter operator (+ - * / %): ")

            if operator == "+":
                result += value
            elif operator == "-":
                result -= value
            elif operator == "*":
                result *= value
            elif operator == "/":
                if value != 0:
                    result /= value
                else:
                    print("❌ Cannot divide by zero")
            elif operator == "%":
                result %= value
            else:
                print("❌ Invalid operator")

            print("Current Result:", result)

        except ValueError:
            print("❌ Please enter valid number")

    print("Final Result:", result)


calculator()