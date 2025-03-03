import timeit
import random
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def add(self, value):
        new_node = Node(value)
        new_node.next = self
        self.prev = new_node
        return new_node 


    def middle(start, last):

        if start is None:
            return None

        slow = start
        fast = start

        while fast != last and fast.next != last:
            fast = fast.next
            if fast != last:
                slow = slow.next
                fast = fast.next

        return slow
      
    def binary_search(head, value):
       
        start = head
        last = None

        while start != last:
            mid = Node.middle(start, last)
            if mid is None:
                return None

            if mid.data == value:
                return mid  
            elif mid.data < value:
                start = mid.next  
            else:
                last = mid 

        return None

class Array:
    def __init__(self, elements):
        self.array = sorted(elements)
    
    def binary_search(self, value):
        low = 0
        high = len(self.array) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.array[mid] == value:
                return mid
            elif self.array[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
def run_linked_list_search(head, n):
    value = random.choice(range(n))
    Node.binary_search(head, value)

def run_array_search(arr, n):
    value = random.choice(range(n))
    arr.binary_search(value)


def measure_linked_list_search_time(n, iterations):
    head = Node(0)
    for value in range(1, n):
        head = head.add(value)
    total_time = timeit.timeit(lambda: run_linked_list_search(head, n), iterations)
    avg_time = total_time / iterations
    return avg_time

def measure_array_search_time(n, iterations):
    elements = list(range(n))
    arr = Array(elements)
    total_time = timeit.timeit(lambda: run_array_search(arr, n), iterations)
    avg_time = total_time / iterations
    return avg_time

def performance_measurements():
    sizes = [1000, 2000, 4000, 8000]
    linked_times = []
    array_times = []
    for n in sizes:
        linked_time = measure_linked_list_search_time(n, 1000)
        array_time = measure_array_search_time(n, 1000)
        linked_times.append(linked_time)
        array_times.append(array_time)
        
    plt.figure()
    plt.plot(sizes, linked_times, marker='o', label='Linked List')
    plt.plot(sizes, array_times, marker='o', label='Array')
    plt.xlabel('Input Size')
    plt.ylabel('Average Search Time')
    plt.title('Binary Search')
    plt.show()

    return None

def main():
    #testing linked
    head = Node(2)
    head = head.add(5)
    head = head.add(7)
    head = head.add(11)
    head = head.add(15)
    head = head.add(18)
    search_value = 7
    result = Node.binary_search(head, search_value)
    print(result.data)
    #testing arr
    arr = Array([10, 20, 30, 40, 50])
    search_index = arr.binary_search(30)
    print(f"{arr.array[search_index]} at: {search_index}")
    #question 5
    performance_measurements()

if __name__ == '__main__':
    main()
