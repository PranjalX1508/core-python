tmp = int (input("temperature :"))
if tmp < 0:
    print("freezing weather")
elif tmp >= 0 and tmp < 10:
    print("very cold")
elif tmp >= 10 and tmp < 20:
    print("cold")
elif tmp >= 20 and tmp < 30:
    print("Hot ")
elif tmp >= 30 and tmp < 40:
    print("its  hot")
else:
    print(" hot very hot")