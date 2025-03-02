import timeit
import numpy as np
import matplotlib.pyplot as plt
import random

# 3:
def linearSearch(li, key):
    for i in range(len(li)):
        if li[i] == key:
            return i
    return -1

def binarySearch(li, key):
    left = 0
    right = len(li) - 1
    while (left <= right):
        mid = (left + right) // 2
        if li[mid] == key:
            return mid
        elif(li[mid]< key):
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 4. linear and binary has a worst case of O(n) and O(logn) respectively
# 5.
def main():
    sizes = [1000,2000,4000,8000,16000,32000]
    trialRun = 100
    
    binTimeArr = []
    linTimeArr = []
    
    for size in sizes:
        array = list(range(size))
        target = random.choice(array)
        
        linTime = timeit.timeit(lambda: linearSearch(array, target), number= trialRun)
        binTime = timeit.timeit(lambda: binarySearch(array, target), number= trialRun)
        
        print(f"time taken for linear search with an array of {size} elements is {linTime}")
        print(f"time taken for binary search with an array of {size} elements is {binTime}")
        
        binTimeArr.append(binTime)
        linTimeArr.append(linTime)
        
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, linTimeArr, marker='o', label='Linear Search', color='red')
    plt.plot(sizes, binTimeArr, marker='s', label='Binary Search', color='blue')
    plt.xlabel('Array Size')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Linear Search vs Binary Search Performance')
    plt.legend()
    plt.grid()
    plt.show()
    
if __name__ == "__main__":
    main()
        
        
        
