def dig_pow(n, p):
    digits = [int(digit) for digit in str(n)]
    
    total_sum = 0
    
    for i in range(len(digits)):
        total_sum += digits[i] ** (p + i)
    
    if total_sum % n == 0:
        return total_sum // n
    else:
        return -1