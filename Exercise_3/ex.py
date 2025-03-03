import sys
import timeit
from matplotlib import pyplot as plt

#1. At line 70 of lists.c, we find the strategy used to grow a full array. It essentially takes new_size, multiplies by 9/8, adds 6, and then replaces the final 2 bits with 0 to get a multiple of 4.

#5. For the majority of the runs, it took about the same amount of time to grow an array of size S to S + 1 than it did to grow of size S - 1 to size S. However, for the runs that took more than the average time, it can take much more time to grow an array from size S to size S + 1 than it did to grow an array of size S - 1 to size S.
# This is because those worst cases are likely to be when the array must move, and it will take more time to move a larger array.

def main():
    the_list = []
    prev_size = 0
    for i in range(0, 65):
        if i > 0:
            the_list.append(i)
        list_size = sys.getsizeof(the_list)
        x = 64
        int_size = (x.bit_length() + 7) // 8
        print(f"New list size = {list_size}, Int size = {int_size}, Capacity = {len(the_list)}")

    list_plus = [i for i in range(0, 65)]
    list_minus = [i for i in range(0, 53)]
    
    result_plus = []
    result_minus = []
    x = []
    
    for i in range(1, 1001):
        list_plus_copy = list_plus.copy()
        list_minus_copy = list_minus.copy()
        result_plus.append(timeit.timeit(lambda:list_plus_copy.append(65), number= 1))
        result_minus.append(timeit.timeit(lambda:list_minus_copy.append(54), number= 1))
        x.append(i)

    plt.figure(figsize=(20, 10))
    
    plt.subplot(1, 2, 1)
    plt.hist(result_plus, 20, histtype='bar', label='S + 1', color='red')
    plt.title('S + 1')
    
    plt.subplot(1, 2, 2)
    plt.hist(result_minus, 20, histtype='bar', label='S - 1', color='Blue')
    plt.title('S - 1')
    
    plt.show()

if __name__ == '__main__':
    main()