def sum_array(arr):
    if not arr:
        return 0
    if len(arr) < 2:
        return 0
    nums = sorted(arr)
    result = 0
    for i in range(1, len(nums) - 1):
        result += nums[i]
    return result
​