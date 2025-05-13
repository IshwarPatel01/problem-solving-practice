 
def remove_smallest(numbers):
    if len(numbers) == 0: return []
    nums = numbers[:]
    smallest_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[smallest_index]:
            smallest_index = i
    
    del nums[smallest_index]
    return nums