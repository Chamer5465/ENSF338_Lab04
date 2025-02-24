class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

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

            if mid == None:
                return None

            if mid.data == value:
                return mid  

            elif mid.data < value:
                start = mid.next  
            else:
                last = mid 

        return None
    
class Array:
    def __init__(self,data):
        self.data=data
    
    def push(self,data):
        self.push(data)
    
    def peek(self,data):
        return self.peek()

class Array:
    def __init__(self, elements=None):
        self.array = sorted(elements)
    
def main():
    #linked list
    head = Node(2)
    head.next = Node(5)
    head.next.next = Node(7)
    head.next.next.next = Node(11)
    head.next.next.next.next = Node(15)
    head.next.next.next.next.next = Node(18)

    search = Node.binary_search(head, 7)
    print(f"result: {search.data}")

    #array WIP
    arr = Array([10, 20, 30, 40, 50])
    print(arr.array)


if __name__ == '__main__':
    main()
