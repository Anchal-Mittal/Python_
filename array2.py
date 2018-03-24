import array
def array_int():
    ar=array.array('I',[1,2,3,4,5,6,7,8,9]) #unsigned array;
    for i in range(0,9):
        print(ar[i],end=" ")
    print("")
    print(ar.typecode) #find the type of the element in the array
    print(ar.itemsize) #give the size of single element in byte
    print(ar.buffer_info()) #returns a tuple representing the address in which array is stored and number of elemnts in it.
    print(ar.buffer_info) #only give the address in which array is stored

array_int();
