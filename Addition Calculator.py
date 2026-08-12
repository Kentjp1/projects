
print("welcome to my calculator")
a= float(input("Enter first number(1-100):"))
b= float(input("Enter second number(1-100):"))
jumlah = a + b
if a>100 or b>100:
    print("invalid number")
else:
    print(f"jumlahnya adalah: {jumlah}")