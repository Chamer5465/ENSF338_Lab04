import timeit
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, node):
        node.next = self.head
        self.head = node

    def insert_tail(self, node):
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def get_size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def get_element_at_pos(self, pos):
        current = self.head
        index = 0
        while current and index < pos:
            current = current.next
            index += 1
        return current

    def reverse(self):
        newhead = None
        prevNode = None
        size = self.get_size()
        for i in range(size - 1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newhead


#Optimised by reducing overall "moving" operations
    def reverse_optimized(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

def create_linked_list(n):
    Linked = LinkedList()
    for i in range(n):
        Linked.insert_tail(Node(i))
    return Linked

def time_reverse_unoptimised(n, iterations):
    average_time = timeit.timeit(lambda: create_linked_list(n).reverse(), number=iterations)/iterations
    return average_time

def time_reverse_optimised(n, iterations):
    average_time = timeit.timeit(lambda: create_linked_list(n).reverse_optimized(), number=iterations)/iterations
    return average_time

def main():
    sizes = [1000, 2000, 3000, 4000]
    iterations = 100

    times_inefficient = []
    times_optimized = []

    for n in sizes:
        time_ineff = time_reverse_unoptimised(n, iterations)
        time_opt = time_reverse_optimised(n, iterations)
        times_inefficient.append(time_ineff)
        times_optimized.append(time_opt)
        print(f"Size: {n}, Unopt Reverse: {time_ineff:.6f} sec, Optimized Reverse: {time_opt:.6f} sec")

    plt.figure()
    plt.plot(sizes, times_inefficient, marker='o', label='Inefficient Reverse')
    plt.plot(sizes, times_optimized, marker='o', label='Optimized Reverse')
    plt.xlabel("List Size")
    plt.ylabel("Average Reverse Time")
    plt.title("Reverse Methods")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
