def check_exam(arr1, arr2):
    total = 0
    n = len(arr1)
​
    for i in range(n):
        if arr1[i] == arr2[i]:
            total += 4
        elif arr2[i] == "":
            continue  # Blank answer → 0 points
        else:
            total -= 1  # Wrong answer → -1 point
​
    return max(total, 0)  # Ensure total is never negative
​