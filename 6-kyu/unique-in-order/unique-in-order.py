 
def unique_in_order(sequence):
#     if not sequence:
#         return []
#     arr = []
​
#     n = len(sequence)
#     for i in range(1,n):
#         if sequence[i-1] != sequence[i]:
#             arr.append(sequence[i-1])
#     if not arr or arr[-1] != sequence[-1]:
#         arr.append(sequence[-1])
#     return arr
    result = []
    for item in sequence:
        if not result or item != result[-1]:
            result.append(item)
    return result