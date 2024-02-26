
class Queue:
    def __init__(self) -> None:
        self.qu = []

    def enqueue(self, x):
        self.qu.append(x)
    
    def dequeue(self):
        q = self.qu.pop(0)
        print(q)
    
    def empty(self):
        print(self.qu == [])
    
    def __str__(self) -> str:
        return str(self.qu)
    

if __name__ == '__main__':
    q = Queue()
    q.enqueue(4)
    print(q)
    q.enqueue(8)
    print(q)
    q.enqueue(1)
    print(q)
    q.dequeue()
    print(q)
    q.enqueue(7)
    print(q)
    q.dequeue()
    print(q)
