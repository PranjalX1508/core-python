account_bal = float(input("  enter amount:"))
withdrawl_amount= int(input("enter withdrawl amount "))

if withdrawl_amount >= 0:
    if account_bal >= withdrawl_amount:
        if withdrawl_amount %100==0:
            print("withdrawl succss")