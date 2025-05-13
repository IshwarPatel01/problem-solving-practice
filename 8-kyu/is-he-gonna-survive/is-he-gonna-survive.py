def hero(bullets, dragons):
    if bullets == 0:
        return False
    
    n = bullets * 2
    if n % dragons == 0:
        return True
    return False