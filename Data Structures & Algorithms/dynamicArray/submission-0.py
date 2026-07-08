class DynamicArray:
    
    def __init__(self, capacity: int):
        self.lst = []
        self.cap = capacity

    def get(self, i: int) -> int:
        return self.lst[i]

    def set(self, i: int, n: int) -> None:
        self.lst[i] = n

    def pushback(self, n: int) -> None:
        if len(self.lst) >= self.cap:
            self.resize()
        self.lst.append(n)

    def popback(self) -> int:
        return self.lst.pop()

    def resize(self) -> None:
        self.cap *= 2

    def getSize(self) -> int:
        return len(self.lst)
    
    def getCapacity(self) -> int:
        return self.cap