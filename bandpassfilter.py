class BandPass():

    def __init__(self, low, high, arr):
        self.low = low
        self.high = high
        self.arr = arr

    def validator(self):
        if all(isinstance(x, int) for x in self.arr):
            return self.arr
        else:
            raise ValueError('Invalid input')

    def filter(self):
        for i in range(len(self.arr)):
            if self.arr[i] < self.low:
                self.arr[i] = self.low
            elif self.arr[i] > self.high:
                self.arr[i] = self.high
        return self.arr