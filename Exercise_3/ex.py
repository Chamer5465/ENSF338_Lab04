import sys
import timeit

#1. At line 70 of lists.c, we find the strategy used to grow a full array. It essentially takes new_size, multiplies by 9/8, adds 6, and then replaces the final 2 bits with 0 to get a multiple of 4.

def main():
    the_list = []
    prev_size = 0
    for i in range(0, 100):
        if i > 0:
            the_list.append(i)
        list_size = sys.getsizeof(the_list)
        x = 64
        int_size = (x.bit_length() + 7) // 8
        print(f"New list size = {list_size}, Int size = {int_size}, Number of capacity = {len(the_list)}")

    list_plus = [i for i in range(0, 65)]
    result_plus = timeit.timeit(lambda:list_plus.copy().append(65), number= 1000) / 1000
    list_minus = [i for i in range(0, 54)]
    result_minus = timeit.timeit(lambda:list_minus.copy().append(54), number= 1000) / 1000

    print(result_plus)
    print(result_minus)

if __name__ == '__main__':
    main()