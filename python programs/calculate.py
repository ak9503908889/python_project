num1=int(input("enter number1:"))
num2=int(input("enter number2:"))

operator =input("enter operator:")

match operator:
    case "+":
        print("sum is",num1+num2)

    case "-":
        print("difference is",num1-num2)
    case "/":
        print("division is ",num1/num2)
    case "*":
        print ("multification is",num1*num2)
    case _:
        print ("enter a valid oprator")


