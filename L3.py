# LEETCODE: 344. Reverse string
def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s
#2 pointer approach

#Finding min and max in an array
def findMinMax(arr):
    if not arr:
        return None, None
    min_val = max_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return min_val, max_val