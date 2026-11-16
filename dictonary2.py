dic = { 'a' : 89, 'b' : 12 , 'c' :90 , 'd' : 78}
min = dic['a']
max = dic['b']
for i in dic.values():
    if i > max: #and i < min:
        max =i
        print(f"Number is greater:{max}")
    if i < min:
        min = i
        print(f"Number is smaller:{min}")