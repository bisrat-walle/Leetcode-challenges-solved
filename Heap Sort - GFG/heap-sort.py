#User function Template for python3

class Solution:
    def heapify(self,arr, n, i):
        largest = i
        left_child, right_child = self.getChildren(arr, i)
        if left_child >= n:
            return
        if arr[largest] < arr[left_child]:
            largest = left_child
        if right_child < n and arr[largest] < arr[right_child]:
            largest = right_child
        if largest == i:
            return
        arr[i], arr[largest] = arr[largest], arr[i]
        self.heapify(arr, n, largest)
            
    def buildHeap(self,arr,n):
        for i in reversed(range(n//2)):
            self.heapify(arr, n, i)
    
        
    def HeapSort(self, arr, n):
        n = len(arr)
        self.buildHeap(arr, n)
 
        
        for i in reversed(range(1, n)):
            arr[i], arr[0] = arr[0], arr[i] 
            self.heapify(arr, i, 0)
    
    def getChildren(self, heap, index):
        right_index = 2*(index+1)
        return right_index-1, right_index
    
    def getParentIndex(self, heap, index):
        parent_index = (index+1)//2-1
        return parent_index    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends