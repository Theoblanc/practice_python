def insertSort():
    arr = [9, 6, 7, 3, 5]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
    print(arr)


insertSort()
