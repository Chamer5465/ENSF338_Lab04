## 1. Give an expression for the time complexity of the reverse()

The for-loop iterates n times.
Inside each iteration, get_element_at_pos(i) traverses from the head to the i-th node, which in the worst case is O(n).
Multiplying these gives O(n) × O(n) = O(n²).

### Design an optimized implementation of the same function with better performance. 

Instead of repeatedly traversing the list with a for loop to find the next node, we directly access the node .next pointer to move forward, optimizing the reversal process and eliminating operations.

```python
def reverse_optimized(self):
    prev = None
    current = self.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    self.head = prev
