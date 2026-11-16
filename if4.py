num1 = int(input())
rmain1 = num1%100
num2 = int(input())
rmain2 = num2%100

if rmain1 > rmain2 :
    print(" Num1 is greater" )
elif rmain1 == rmain2:
    print("Num1 is equal to num2")
else :
    print(" Num2 is greater ")