class BandPass():

    def validator(self, arr):
        for item in arr:
            if all(isinstance(x, int) for x in arr):
                return arr
            else:
                return "Invalid input"

    def bandpass(self, min, max, arr):
        for i in range(len(arr)):
            if arr[i] < min:
                arr[i] = min
            elif arr[i] > max:
                arr[i] = max
        return arr