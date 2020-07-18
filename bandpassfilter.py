class BandPass():

    def validator(self, arr):
        return True

    def bandpass(self, min, max, arr):
        for i in range(len(arr)):
            if arr[i] < min:
                arr[i] = min
            elif arr[i] > max:
                arr[i] = max
        return arr