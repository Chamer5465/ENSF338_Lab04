
def processdata(li):
    for i in range(len(li)):    # o(n) complexity
        if li[i] > 5:
            for j in range(len(li)):    # o(n) complexity
                li[i] *= 2
                
# 1. At the best case scenario (which is when no elements in the list
# are > 5) this will be an o(n) complexity as it still has to traverse
# the list once and its worst and average case complexity is when 1 or more
# elements are above 5 it has a complexity of o(n*n)

# 2 modified code where all cases are the same
def processdata(li):
    for i in range(len(li)):    # o(n) coomplexity
        for j in range(len(li)):    # o(n) complexity
            li[i] *= 2
            
# in this modification ive removed the check if the element is above 5
# now at any given input it will traverse the list twice at o(n) complexity
# giving it a total complexity of o(n*n)
