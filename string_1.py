#str = input("Enter Any String:")
#words = str.split()
#print("Total words :", len(words))


str = input("Enter Any string:")
count=1
for i in str:
    if i == " ":
        count+=1;
print(f"Count :{count}")