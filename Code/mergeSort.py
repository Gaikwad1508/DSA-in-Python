def mergeSort(arr, s, e):
    if s==e:
        return
    
    mid=(s+e)//2
    mergeSort(arr, s, mid)
    mergeSort(arr, mid+1, e)

    #Create two subparts of main array 
    left=arr[s:mid+1]
    right=arr[mid+1:e+1]

    i, j, k = 0, 0, s

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
            k+=1
        elif left[i]>right[j]:
            arr[k]=right[j]
            j+=1
            k+=1

    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1

arr=[99, 0, 15, -12, 17, 49, 46, 39]
mergeSort(arr, 0, len(arr))
print(arr)