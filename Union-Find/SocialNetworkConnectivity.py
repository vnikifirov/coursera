N = 1000
def random_pair():
    a = random.randint(0, N-1)

    b = a
    while a == b:
        b = random.randint(0, N-1)

    return (a, b)

for i in xrange(N * (N-1)):   
    pair = random_pair()
    print("{0}, {1}, {2}".format(pair[0], pair[1], i))