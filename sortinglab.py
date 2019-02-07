

def bubbleSort(priceList):
    for passnum in range(len(priceList)-1,0,-1):
        for i in range(passnum):
            if priceList[i]<priceList[i+1]:
                temp = priceList[i]
                priceList[i] = priceList[i+1]
                priceList[i+1] = temp

priceList = [0.99, 1.25, 2.35, 2.99, 0.79]
bubbleSort(priceList)
print("Price List Bubble")
print(priceList)


def selectionSort(priceList):
   for fillslot in range(len(priceList)-1,0,-1):
       maxpos=0
       for location in range(1,fillslot+1):
           if priceList[location]<priceList[maxpos]:
               maxpos = location

       temp = priceList[fillslot]
       priceList[fillslot] = priceList[maxpos]
       priceList[maxpos] = temp

priceList = [0.99, 1.25, 2.35, 2.99, 0.79]
selectionSort(priceList)
print("Price List Selection")
print(priceList)



def selectionSort(nlist):
   for fillslot in range(len(nlist)-1,0,-1):
       maxpos=0
       for location in range(1,fillslot+1):
           if nlist[location]>nlist[maxpos]:
               maxpos = location

       temp = nlist[fillslot]
       nlist[fillslot] = nlist[maxpos]
       nlist[maxpos] = temp



nlist = ['apples', 'peaches', 'pears', 'grapes', 'bananas']
selectionSort(nlist)
print("Fruit List Selection")
print(nlist)


def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

bubbleSort(nlist)
print("Fruit List Bubble")
print(nlist)


