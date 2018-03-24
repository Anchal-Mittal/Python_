def sort():
    array=[5,7,1,3,9,2]

    for i in range(0,5):
        for j in range(i+1,6):
            if array[i]>=array[j] :
                x=array[i]
                array[i]=array[j]
                array[j]=x

    print(array)
    

sort();
