#!/usr/bin/env python3
def add_arrays(ar1, ar2):
    if len(ar1) == len(ar2):
        result = []
        for i in range(len(ar1)):
            result.append(ar1[i] + ar2[i])
        return result
    return None
arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
print(add_arrays(arr1, arr2))
print(arr1)
print(arr2)
print(add_arrays(arr1, [1, 2, 3]))

