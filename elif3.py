age = input("enter age" )
gen = input(" enter gender")
if age >= 18 and age <= 25 and gen == 'female' :
    print("elegible for Women scholarship")
elif gen == 'male' :
    print(" Not elegible for Women scholarship")
else :
    print("Not elegible for anyscholarship")