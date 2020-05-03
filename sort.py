#Author: Daniel Rosel
#Date: 5/1/2020
#all my code
import random
from matplotlib import pyplot as plt
import array

##code
def sortArray(arr):
    print("initial ARR:",arr)
    x = list()
    for it in range(len(arr)):
        x.append(it)
    plt.scatter(x, arr)
    for x in range(len(arr)):
        for n in range(len(arr)-1):   
            #print(arr[n],arr[n+1])   just to debug
            if arr[n]>=arr[n+1]:
                temp1 = arr[n]
                temp2 = arr[n+1]
                arr[n]=temp2
                arr[n+1]=temp1
            else:
                continue
    print("SORTED: ", arr)    
    plt.plot(arr)
    plt.show()
    return arr
#data to sort

array = list()
for nb in range(random.randint(50, 100)): #just to have some fun with it
    array.append(random.randint(0, 200))
SongSorted = sortArray(arrray)