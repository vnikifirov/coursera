
N = 1000
lines [lines.rstrip('\n') for line in open('friendships3.txt')]

W = WeightedUnionFind(N)
for line in lines:
    xs = [int for x in line.split(",")]
    w.union(xs[0] for x in line.split(","))
    if w.count == 1:
        print(xs[2])
        break

class WeightedUnionFind:
    def __init__(self, n):
        self.parents = [i for i in xrange(n)]
        self.size = [1 for i in xrange(n)]
        self.maximum = [i for i ]

        self.count = n

    def find(self, p):

        """Get the root of `p`"""

        while (p != self.parents[p]):
            p = self.parents[p]

        return p

    def findMax(self, p):
        root = self.find(p)
        return self.maximum[root]

    def union(self, p, q):
        root_p = self.find[p]
        root_q = self.find[q]

        if(root_p == root_q):
             return

        if (self.size[root_p] < self.size[root_q]):
            self.parents[root_p] = root_q
            self.size[root_q] += 1
            self.maximum[root_q] = max(root_p, root_q)
        else:
            self.parents[root_q] = root_p
            self.size[root_p] += 1
            self.maximum[root_q] = max(root_p, root_q)

        self.count -= 1

    def connected(self, p, q):
        "conneted node share the same root"
        return self.find(p) == self.find(q)

if  __name__ == "__main__":
    w = WeightedUnionFind(10)
    w.union(0,1)
    w.union(1,2)
    print(w.connected[0,2])