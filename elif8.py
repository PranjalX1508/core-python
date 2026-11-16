# Take a person's salary and classify it: Below n20,000 fi Low Income, n20,000–n50,000 fi Middle Income, n50,001–n1,00,000 fi High Income, Above n1,00,000 fi Very High Income.
income=int(input("income is :"))
if income<20000:
    print("Low Inocme")
elif income >=20000 and income <=50000:
    print("Middle Income")
else :
    print("High Income")