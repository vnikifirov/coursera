class Successor:

    def __init__(self, n):
        self.top = range[1, n] + [None]
        self.bottom = range[1, n] + [None]

    def succ(self, x):
        return self.bottom[x]

    def remove(self, x):

        _from = self.top[x]
        _to = self.bottom[x]

        if _from != None:
            self.bottom[_from] = _to

        if _to != None:
            self.top[_to] = _from
        
        self.top[x] = None
        self.bottom[x] = None
