def bandpass(min, max, arr):
    for i in range(len(arr)):
        if arr[i] < min:
            arr[i] = min
    return arr