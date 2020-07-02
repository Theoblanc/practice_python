def bubbleSort():
    arr = [9, 6, 7, 3, 5]

    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(arr)


bubbleSort()
