def count_sheeps(sheep):
    count = 0
    if len(sheep) == 0:
        return count
    
    for i in sheep:
        if i == True:
            count += 1
    
    return count
  # TODO May the force be with you