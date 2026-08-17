print("To find the largest number")
a = float(input("Enter first number a: "))
b = float(input("Enter second number b: "))
c = float(input("Enter third number c: "))
if a == b == c:
    print("All are equal")
elif a> b and a>c:
    print("a is greatest")
elif b>c and b>a:
    print("b is greatest")
elif c>a and c>b:
    print("c is greatest")
elif a==b and a>c:
    print("a and b are the greatest")
elif b==c and b>a:
    print("b and c are the greatest")
elif a==c and a>b:
    print("a and c are the greatest")