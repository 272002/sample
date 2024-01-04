def bubble(arrayList):
    swap = False
    for i in range(len(arrayList)-1):
        swap = False
        for j in range(len(arrayList) - i - 1):
            if arrayList[j]>arrayList[j+1]:
                arrayList[j],arrayList[j+1] = arrayList[j+1],arrayList[j]
                swap = True
        
        if swap == False:
            break

    for i in range(len(arrayList)):
        print(arrayList[i],end=" ")
    
arrayList = [64, 25, 12, 22, 11]
bubble(arrayList)
