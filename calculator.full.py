def calculator():
    result=0

    
    while True:
         value=float(input("Enter the value of input: "))

         operator = input("Enter an operator (+ - * / %): ") 
         if value == 0:
                break
         elif operator =="+":
                result += value
         elif operator =="-":
                result -= value
         elif operator =="*":
                result *= value
         elif operator =="/":
                result /= value 
         elif operator =="%":
                result %= value
    print(result)

calculator()