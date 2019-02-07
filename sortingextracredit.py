def bubbleSort(priceList):
    for passnum in range(len(priceList)-1,0,-1):
        for i in range(passnum):
            if priceList[i]<priceList[i+1]:
                temp = priceList[i]
                priceList[i] = priceList[i+1]
                priceList[i+1] = temp


Fruitlist = ['apples', 'peaches', 'pears', 'grapes', 'bananas']
sortedFruitList = ['apples', 'peaches', 'pears', 'grapes', 'bananas']
priceList = [0.99, 1.25, 2.35, 2.99, 0.79]
bubbleSort(priceList)

area0 = priceList.index(0.99)
area1 = priceList.index(1.25)
area2 = priceList.index(2.35)
area3 = priceList.index(2.99)
area4 = priceList.index(0.79)

print(area0,area1,area2,area3,area4)

sortedFruitList[0] = Fruitlist[area0]
sortedFruitList[1] = Fruitlist[area1]
sortedFruitList[2] = Fruitlist[area2]
sortedFruitList[3] = Fruitlist[area3]
sortedFruitList[4] = Fruitlist[area4]


print(sortedFruitList)
print(priceList)
