arrayInput = [6,5,4,3,2,1]
    
def insertionSort(arr,n):
    for i in range(1,n):
        j = i
        while j>0 and arr[j-1]>arr[j]:
            temp = arr[j-1]
            arr[j-1]= arr[j]
            arr[j] = temp
            j-=1
        
        print(arr)
    
    
insertionSort(arrayInput,6)

Output

[5, 6, 4, 3, 2, 1]
[4, 5, 6, 3, 2, 1]
[3, 4, 5, 6, 2, 1]
[2, 3, 4, 5, 6, 1]
[1, 2, 3, 4, 5, 6]
