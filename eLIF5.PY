#. Take a person's age and classify them: 0–12 fi Child, 13–19 fi Teenager, 20–59 fi Adult, 60+ fi Senior Citizen.

age = int(input("Age is:"))
if age >=0 and age <=12:
    print("Child ")
elif age >=13 and age <=19:
    print("Teenager")
elif age >= 20 and age <= 59 :
    print("Adult")
else :
    print("Senior citizen")