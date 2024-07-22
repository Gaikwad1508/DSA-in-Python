def partition(arr, s, e):
    #suppose pivote element is arr[s]
    pivot=arr[s]
    cnt=0                               #count to store no. of numbers less than pivot element
    for i in range(s+1, e+1):
        if arr[i]<=pivot:
            cnt+=1

    pivotIndex=s+cnt
    #putting pivote element at pivote index
    arr[s], arr[pivotIndex]=arr[pivotIndex], arr[s]

    # making all elements left to pivot element are less and all elements right to it are greater
    i, j=s, e
    while i<pivotIndex and j>pivotIndex:
        while i<pivotIndex and arr[i]<=pivot:
            i+=1
        while j>pivotIndex and arr[j]>=pivot:
            j-=1
        if i<pivotIndex and j>pivotIndex:
            arr[i], arr[j]=arr[j], arr[i]
            i+=1
            j-=1

    return pivotIndex

def quickSort(arr, s, e):
    #base condition
    if s>=e:
        return
    
    #Index of pivot element
    p=partition(arr, s, e)

    #recursively sorting left part
    quickSort(arr, s, p-1)

    #recursively sorting right part
    quickSort(arr, p+1, e)


#Function call
arr=[99, 23, 45, 12, 34, 9, 89]
quickSort(arr, 0, len(arr)-1)
print(arr)
