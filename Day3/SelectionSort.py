arrayInput = [13,46,24,52,20,9]

def selectionSort(arr,n):
    for i in range(0,n-1):
        min = i
        for j in range(i,n):
            if arr[j] <= arr[min]:
                min = j
            
            
        #swap
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp 
        
    print(arr)
    
selectionSort(arrayInput,6)
