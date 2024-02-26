

class Stack:
    
    def __init__(self) -> None:
        self.st = []
    
    def push(self, x):
        self.st.append(x)

    def pop(self):
        s = self.st.pop()
        print(s)

    def peak(self):
        print(self.st[-1])

    def empty(self):
        print(self.st == [])

    def size(self):
        print(len(self.st))
    
    def __str__(self):
        return str(self.st)


if __name__ == '__main__':
    s = Stack()
    s.push(8)
    print(s)
    s.push(6)
    print(s)
    s.push(7)
    print(s)
    s.pop()
    print(s)
    s.push(5)
    print(s)
    s.pop()
    print(s)
