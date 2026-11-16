str = input("Enter any string:")
str_1=""
str_2=""

for i in range(len(str)):
    if i % 2==0:
        str_1 += str[i]
    else:
        str_2 += str[i]

print(f"String 1:{str_1}")
print(f"String 2s:{str_2}")