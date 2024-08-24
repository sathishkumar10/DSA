arrayInput = [13,46,24,52,20,9]
    
def bubbleSort(arr,n):
    # for loop starts from last index to 1
    for i in range(n-1,0,-1):
        didSwap = 0
        for j in range(0,i):
            if(arr[j]> arr[j+1]):
                didSwap=1
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        print(arr)
        if didSwap == 0:
            break;
    
bubbleSort(arrayInput,6)
