def no_space(x):
    #your code here
#     return x.replace(" ", "")
​
    result = ""
    
    for i in x:
        if i != " ":
            result += i
​
    return result