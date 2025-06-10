def get_real_floor(american_floor):
    """
    Converts an American floor number to a European floor number.
​
    Args:
        american_floor (int): The floor number in the American system.
​
    Returns:
        int: The corresponding floor number in the European system.
             - Basements (negative numbers) remain unchanged.
             - The American 1st floor becomes the European 0 (ground) floor.
             - Floors above American 13th are adjusted by subtracting 2
               (for the skipped 1st floor and 13th floor).
    """
    if american_floor < 1:
        # Basements (negative floors) are the same in both systems
        return american_floor
    elif american_floor == 1:
        # American 1st floor is European ground floor (0)
        return 0
    elif american_floor <= 13:
        # For American floors 2 to 12, subtract 1 (for the ground floor)
        return american_floor - 1
    else:
        # For American floors above 13, subtract 2
        # (for the ground floor and the skipped 13th floor)
        return american_floor - 2