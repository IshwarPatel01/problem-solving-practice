def tribonacci(signature, n):
    if n == 0:
        return []
    signature = signature[:n]
    length = n - len(signature)
    for i in range(length):
        total = 0
        for j in range(-1,-4,-1):
            total += signature[j]
        signature.append(total)
    return signature
            