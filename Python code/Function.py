"""def add():
    x=10
    y=20
    z=x+y
    print("add is",z)
add()"""

"""def fruit(name,fruit):
    print(name,"like",fruit)
fruit("anjali","mango")
fruit("nilesh","apple")
fruit("simran","orange")"""
def table(no):
    if no<=50:
        print(no,end=" ")
        no=no+5
        table(no)
table(5)
