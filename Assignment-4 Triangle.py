def my_func():
    print("hello user")
    
def triangle():
    s1 = int(input("Enter length of first side"))
    s2 = int(input("Enter length of second side"))
    s3 = int(input("Enter length of third side"))
    if s1 == s2 == s3:
        print("The traingle is: Equilateral triangle")
    elif s1 == s2 and s2 != s3:
        print("The traingle is: Isosceles triangle")
    elif s2 == s3 and s2 != s1:
        print("The traingle is: Isosceles triangle")
    else:
        print("The traingle is: Scalene Traingle")
    
my_func()
triangle()