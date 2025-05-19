def array_diff(a, b):
    for n in b:
        while n in a:
            a.remove(n)
    return a
    
#     if len(a) or len(b) == 0:
#         return []
    
#     arr = []
    
#     for i in a:
#         for j in b:
#             if i == j:
#                 break
#             else:
#                 arr.append(i)
#     return arr