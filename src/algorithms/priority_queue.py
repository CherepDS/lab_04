# Реализация приоритетной очереди с помощью двоичной кучи
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)
    
    def __bool__(self):
        return len(self.heap) > 0
    
    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1)//2
            if self.heap[parent] <= self.heap[index]:
                break
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent

    def _sift_down(self, index):
        size = len(self.heap)

        while True:
            left = index*2 + 1
            right = index*2 + 2
            
            smallest = index
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if smallest == index:
                break

            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            index = smallest
        
    def put(self, item):
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)
    
    def get(self):
        if not self.heap:
            raise IndexError("Priority queue is empty")

        result = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._sift_down(0)

        return result

    def next(self):
        if not self.heap:
            raise IndexError("Priority queue is empty")
        return self.heap[0]