def reverse(st):
    words = st.split()
    result = ""
    for i in range(len(words) - 1, -1, -1):
        result += words[i] + " "
    return result.strip()  # Remove trailing space
​