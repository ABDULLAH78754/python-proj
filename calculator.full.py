def calculator():
    result=0

    
    while True:
         value=float(input("Enter the value of input: "))

          
         if value == 0:
                break
         else:
              operator = input("Enter an operator (+ - * / %): ")
              if operator =="+":
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