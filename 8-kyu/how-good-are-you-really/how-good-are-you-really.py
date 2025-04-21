 
def better_than_average(class_points, your_points):
    total = 0
    n = len(class_points)
    for i in class_points:
        total += i
    total += your_points
    average = total // (n + 1)
    return True if average < your_points else False
    