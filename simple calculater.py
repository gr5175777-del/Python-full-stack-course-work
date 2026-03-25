x = int(input("enter first number:"))
y = int(input("enter second number:"))
ch = input("enter any operator(+,-,*,/,%):")
if ch== "+":
    print(x+y)
elif ch== "-":
    print(x-y)
elif ch== "*":
    print(x*y)
elif ch== "/":
    print(x/y)
elif ch== "%":
    print(x%y)
else:
    print("select a vaild operator")
