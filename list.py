def d():
    print("creating the list: ")
    list1 =[1,0,4,-2,3]
    list2 =['a','4','5','z','d','f']

    print(list1)
    print(list2)
    print("length of list1=")
    print(len(list1))

    list1.sort()
    print(list1)

    print("length of list2=")
    print(len(list2))

    print("maximum elements of list2=")
    print(max(list2))

    print("minimum elements of list2")
    print(min(list2))

    del list1[3] #deleting 3 element from the list
    print(list1)

    print("length of list1 after updating ")
    print(len(list1))

    print(list1[1:]) #slicing

    seq= 1,3,4,2

    list(seq)

    print(len(seq))
    
    print(seq)

    list1[2]=2991 #adding element at index 2

    print(list1)

d();
