def warn_the_sheep(queue):
    if queue[-1] is 'wolf':
        return 'Pls go away and stop eating my sheep'
    else:
        pos = len(queue) - queue.index('wolf') - 1
        return 'Oi! Sheep number {}! You are about to be eaten by a wolf!'.format(pos)