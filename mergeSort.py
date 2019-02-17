def mergeSort(list):
    lenlist = len(list)
    if(lenlist > 1):
        mid = lenlist//2
        Left = list[:mid]
        Right = list[mid:]
        mergeSort(Left)
        mergeSort(Right)
        i = 0
        j = 0
        k = 0

        while i < len(Left) and j < len(Right):
            if(Left[i] < Right[j]):
                list[k] = Left[i]
                i = i + 1
            else:
                list[k] = Right[j]
                j = k + 1
            k = k + 1
        while i < len(Left):
            list[k] = Left[i]
            i = i + 1
            k = k + 1
        while j < len(Right):
            list[k] = Right[j]
            j = j + 1
            k = k + 1

print("Input list : ")
list = [int(x) for x in input().split()]
mergeSort(list)
print(list)
        
