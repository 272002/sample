def sort(arrayList):
    minidx = 0
    for i in range(len(arrayList)-1):
        minidx = i
        for j in range(i+1,len(arrayList)):
            if arrayList[j]<arrayList[minidx]:
                minidx = j
            
        key = arrayList[minidx]
        k = minidx
        while k > i:
            arrayList[k] = arrayList[k-1]
            k-=1
        arrayList[i] = key
    

    for i in range(len(arrayList)):
        print(arrayList[i],end=" ")
    
arrayList = [64, 25, 12, 22, 11]
sort(arrayList)
