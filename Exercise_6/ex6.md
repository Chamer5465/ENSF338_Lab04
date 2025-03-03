1. 
    Array:
        - Traversal is O(1) because of indexes
        - head insertion is O(n)
        - tail insertion is O(1)
        - insertion for anywhere in between is O(n)
        - deletion without index and anywhere before the tail is O(n)
        - deletion with index and tail deletion are O(1)



    Linked List:
        - traversal is O(n)
        - head insertion is O(1)
        - tail insertion is O(n)
        - insertion for anywhere in between is O(n)
        - head deletion is O(1)
        - tail deletion is O(n)
        - deletion anywhere in between is O(n)

2. 
    The replace cannot reduce the impact of the standalone tasks. The replacement itself (ignoring the standalone tasks) will always be O(1) and is always only dependant on the deletion and insertion themselves. There is only one acception to this, when our value to replace is the same as the value we want to replace it with. In this special case, we can just skip the replacement all together because the value being replaced is already the correct value.

3. 
    Insertion Sort:
        Insertion sort would be a good sorting algorithm to use on a doubly linked list. This is because it goes through and sorts the list sequentially. Therefore, it would be as simple as traversing using the next and previous pointers, and then correctly setting the next and previous pointers when it is in its new place.

    Merge Sort:  
        Merge sort is also a good sorting algorithm to use with a doubly linked list. This is because the nodes are not truly a part of the list, therefore to split and merge, you simply have to remove the next pointer and previous pointer of the elements on either side of the split, and merging is as simple as setting the next pointer and previous pointers at the intersections of the seperate lists you want to merge. 

4.  
    The time complexity of insertion sort remains the same (O(n^2)) and the time complexity for merge sort remains the same (O(nlogn))
