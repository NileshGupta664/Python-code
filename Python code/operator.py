"""x=10
y=15
print("Addition is:",x+y)
print("Subtraction is:",x-y)
print("Multiplication is:",x*y)
print("division is:",x/y)
print("module is:",x%y)"""
x=int(input("enter first number"))
y=int(input("enter second number"))
z=int(input("enter third number"))
if x>z and x>y:
    print(x,"is greatest")
if y>x and y>z:
       print(y,"is greatest")
if z>x and z>y:
       print(z,"is greatest")