import array
def array_int():
    arr=array.array('I',[1,2,3]) #creating unsigned array;
    for i in range(0,3):
        print(arr[i],end=" ") #for space we are using end
    arr1=array.array('i',[1,-2,-3]) #creating signed array;
    print("")
    for i in range(0,3):
        print(arr1[i],end=" ")

array_int();
