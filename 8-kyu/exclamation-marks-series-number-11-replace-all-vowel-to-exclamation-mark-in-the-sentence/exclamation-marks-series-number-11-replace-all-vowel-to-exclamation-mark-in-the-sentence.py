 
def replace_exclamation(st):
    vowel = ["a", "e", "i", "o" ,"u", "A", "E", "I", "O", "U"]
    
    
#     str= st.lower()
    for char in vowel:
        st = st.replace(char, "!")
    
    return st