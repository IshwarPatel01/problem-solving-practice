# n = [2,9,3,6,4,8,5,10]
n = [50, 120, 90, 200, 180]  

max_number = n[0]

for i in n[1:]:
    if i > max_number:
        max_number = i

print(max_number)