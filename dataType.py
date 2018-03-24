def loop():
    print("check long and double data types are not exist")
    print(type(2**3)) # int data type
    print((2**3))
    print(type(2**38)) # int data type not long
    print(type(2*3.9)) # float data type
    print(type(3.8**50)) # float data type not double
    print(type('m'))
    d=9
    print(type(d))
    d=9.1
    print(type(d))
    b=False
    print(type(b))
    print(type("mayank"))

loop();
