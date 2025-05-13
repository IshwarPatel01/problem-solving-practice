def find_short(s):
    # your code here
    str_list = s.split()
    
    j = len(str_list[0])
    
    for i in range(1,len(str_list)):
        if len(str_list[i]) < j:
            j = len(str_list[i])
            
    return j # l: shortest word length
​