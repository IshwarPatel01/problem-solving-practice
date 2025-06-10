 
def multi_table(number):
    answer = ''
    for i in range(1, 11):  # Standard 1 to 10 table
        x = f'{i} * {number} = {i * number}\n'
        answer += x
    return answer.strip()