def swap():
    a=int(input())
    b=int(input())
    print("BEFORE SWAPPING")
    print("a=",a)
    print("b=",b)
    
    a=a^b
    b=a^b
    a=a^b
    print("After swapping two numbers")
    print("a=",a)
    print("b=",b)


swap();    
