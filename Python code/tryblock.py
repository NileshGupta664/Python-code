"""try:
    a=10
    print("value of x:",a)
except:
    print("an exception occured")
else:
    print("this is else statement")"""
try:
    a=10
    b=0
    c=a/b
    print("value of c",c)
except:
    print("Do not put zero in denominator")
else:
     print("this is else statement")
finally:
    print("this is finally block")