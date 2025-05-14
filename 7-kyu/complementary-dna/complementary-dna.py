def DNA_strand(dna):
    # code here
#     haskell = [A,T,G,C]
    result = ""
    for char in dna:
        if char == "A":
            result += "T"
        elif char == "T":
            result += "A"
        elif char == "C":
            result += "G"
        elif char == "G":
            result += "C"
    return result
            