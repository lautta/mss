# algorithm 1
def algorithm1(array):
    n = len(array)
    sub_low = sub_high = max_sum = 0

    for i in range(n):
        for j in range(i, n):
            total = 0
            for k in range(i, j + 1):
                total += array[k]
                if total > max_sum:
                    max_sum = total
                    sub_low = i
                    sub_high = j

    return max_sum, array[sub_low:sub_high + 1]


# algorithm 2
def algorithm2(array):
    n = len(array)
    sub_low = sub_high = max_sum = 0

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += array[j]
            if total > max_sum:
                max_sum = total
                sub_low = i
                sub_high = j

    return max_sum, array[sub_low:sub_high + 1]


# helper function for algorithm 3
def maxSuffix(array, start, end):
    sum = array[end]
    maxSum = array[end]
    value = end

    for i in range(1, (end - start + 1)):
        sum += array[end - i]
        if sum > maxSum:
            maxSum = sum
            value = end - i
    return (maxSum, value)


# helper function for algorithm 3
def maxPrefix(array, start, end):
    sum = array[start]
    maxSum = array[start]
    value = start

    for i in range(1, (end - start + 1)):
        sum += array[start + i]
        if sum > maxSum:
            maxSum = sum
            value = start + i
    return (maxSum, value)


# divide and conquer
# returns the max subarray sum, the start index of the subarray, and the ending index of the subarray
def d_and_c(array, start, end):
    if start == end:
        return (array[start], start, end)

    mid = (end + start) / 2
    L_sum, L_start, L_end = d_and_c(array, start, mid)
    R_sum, R_start, R_end = d_and_c(array, mid + 1, end)

    suf_sum, suf_start = maxSuffix(array, start, mid)
    pref_sum, pref_end = maxPrefix(array, mid + 1, end)

    if L_sum > R_sum:
        if L_sum > (suf_sum + pref_sum):
            return (L_sum, L_start, L_end)
        else:
            return ((suf_sum + pref_sum), suf_start, pref_end)
    else:
        if R_sum > (suf_sum + pref_sum):
            return (R_sum, R_start, R_end)
        else:
            return ((suf_sum + pref_sum), suf_start, pref_end)

# algorithm 3
def algorithm3(array):
    low = 0
    high = len(array) - 1
    (max_sum, sub_low, sub_high) = d_and_c(array, low, high)

    return max_sum, array[sub_low:sub_high + 1]
