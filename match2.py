num1 = int(input("Enter Number 1:"))
num2=int(input("Enter Number 2:"))
choice = input("Enter Choice:")
match choice:
    case '+':
        print("Sum", num1 + num2) 
    case '-':
            print("difference", num1 - num2)
    case '*':
            print("multiplication", num1 * num2)
    case '/':
            print("divide", num1 / num2)
    case _:
            print("error")