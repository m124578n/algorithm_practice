
#  from https://medium.com/@tobby168/%E7%94%A8-python-%E5%AF%A6%E4%BD%9C-binary-heaps-priority-queue-12e0b82ed7b3
class MaxPriorityQueue:
    def __init__(self, array=[]) -> None:
        self.heap = list([None])
        self.length = 0
        if array != []:
            for x in array:
                self.insert(x)

    def insert(self, item):
    # insert item to the end then swim it up
        self.heap.append(item)
        self.length = self.length + 1
        self.__swim(self.length)

    def extractMax(self):
        # exchange first item and last item, then order again
        maximum = self.heap[1]
        self.__exchange(1, self.length),
        self.heap.pop()
        self.length = self.length - 1
        self.__sink(1)
        
        return maximum

    def __swim(self, k):
        # Exchange key in child with key in parent. Repeat until heap order restored.
        while k > 1 and self.__less(k // 2, k):
            self.__exchange(k // 2, k)
            k = k // 2

    def __sink(self, k):
        # Key in parent exchange with ket in larger child. Repeat until heap order restored.
        while k * 2 <= self.length:
            j = k * 2
            if j < self.length and self.__less(j, j + 1):
                j = j + 1

            self.__exchange(k, j)
            k = j
        

    def __less(self, a, b):
        # return a boolean represent if item at a position is less than item at b
        if self.heap[a] < self.heap[b]:
            return True
        else:
            return False
    
    def __exchange(self, a, b):
        # swap item in the heap at position a and b
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp


#####################################################################
#####################################################################
#####################################################################

# from https://www.geeksforgeeks.org/min-heap-in-python/
        
import sys 
  
class MinHeap: 
  
    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1) 
        self.Heap[0] = -1 * sys.maxsize 
        self.FRONT = 1
  
    # Function to return the position of 
    # parent for the node currently 
    # at pos 
    def parent(self, pos): 
        return pos//2
  
    # Function to return the position of 
    # the left child for the node currently 
    # at pos 
    def leftChild(self, pos): 
        return 2 * pos 
  
    # Function to return the position of 
    # the right child for the node currently 
    # at pos 
    def rightChild(self, pos): 
        return (2 * pos) + 1
  
    # Function that returns true if the passed 
    # node is a leaf node 
    def isLeaf(self, pos): 
        return pos*2 > self.size 
  
    # Function to swap two nodes of the heap 
    def swap(self, fpos, spos): 
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 
  
    # Function to heapify the node at pos 
    def minHeapify(self, pos): 
  
        # If the node is a non-leaf node and greater 
        # than any of its child 
        if not self.isLeaf(pos): 
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or 
               self.Heap[pos] > self.Heap[self.rightChild(pos)]): 
  
                # Swap with the left child and heapify 
                # the left child 
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]: 
                    self.swap(pos, self.leftChild(pos)) 
                    self.minHeapify(self.leftChild(pos)) 
  
                # Swap with the right child and heapify 
                # the right child 
                else: 
                    self.swap(pos, self.rightChild(pos)) 
                    self.minHeapify(self.rightChild(pos)) 
  
    # Function to insert a node into the heap 
    def insert(self, element): 
        if self.size >= self.maxsize : 
            return
        self.size+= 1
        self.Heap[self.size] = element 
  
        current = self.size 
  
        while self.Heap[current] < self.Heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 
  
    # Function to print the contents of the heap 
    def Print(self): 
        for i in range(1, (self.size//2)+1): 
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1])) 
  
    # Function to build the min heap using 
    # the minHeapify function 
    def minHeap(self): 
  
        for pos in range(self.size//2, 0, -1): 
            self.minHeapify(pos) 
  
    # Function to remove and return the minimum 
    # element from the heap 
    def remove(self): 
  
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size] 
        self.size-= 1
        self.minHeapify(self.FRONT) 
        return popped 
    

# Python3 program to demonstrate working of heapq 
  
from heapq import heapify, heappush, heappop 
  
# Creating empty heap 
heap = [] 
heapify(heap) 
  
# Adding items to the heap using heappush function 
heappush(heap, 10) 
heappush(heap, 30) 
heappush(heap, 20) 
heappush(heap, 400) 
  
# printing the value of minimum element 
print("Head value of heap : "+str(heap[0])) 
  
# printing the elements of the heap 
print("The heap elements : ") 
for i in heap: 
    print(i, end = ' ') 
print("\n") 
  
element = heappop(heap) 
  
# printing the elements of the heap 
print("The heap elements : ") 
for i in heap: 
    print(i, end = ' ') 

  
# Driver Code 
if __name__ == "__main__": 
      
    print('The minHeap is ') 
    minHeap = MinHeap(15) 
    minHeap.insert(5) 
    minHeap.insert(3) 
    minHeap.insert(17) 
    minHeap.insert(10) 
    minHeap.insert(84) 
    minHeap.insert(19) 
    minHeap.insert(6) 
    minHeap.insert(22) 
    minHeap.insert(9) 
    minHeap.minHeap() 
  
    minHeap.Print() 
    print("The Min val is " + str(minHeap.remove())) 