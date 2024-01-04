def insert(arrayList):
    for i in range(1,len(arrayList)):
        key = arrayList[i]
        j = i-1
        while (j>=0 and arrayList[j]>key):
            arrayList[j+1] = arrayList[j]
            j-=1
        arrayList[j+1] = key


    for i in range(len(arrayList)):
        print(arrayList[i],end=" ")
    
arrayList = [64, 25, 12, 22, 11]
insert(arrayList)
