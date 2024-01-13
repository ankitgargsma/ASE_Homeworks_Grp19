class Num:
    def __init__(self, s, n):
        if( s is None):
            self.s = " "
        else:
            self.s = s
        if( n is None):
            self.at = 0
        else:
            self.at = n
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi = float('-inf')
        self.lo = float('inf')
        #self.heaven = ##TODO

    def add(self, x, d):
        if(x != "?"):
            self.n = self.n + 1
            d = x - self.mu
            self.mu = self.mu + d/self.n
            self.m2  =self.m2 + d*(x - self.mu)
            self.lo =  min(x, self.lo)
            self.hi = max(x, self.hi)
        return self

    def mid(self):
        return self.mu
    
    def div(self):
        return self.n < 2 and 0 or (self.m2/(self.n - 1))^.5
    
    def norm(self,x):
        return x == "?" and x or (x - self.lo)/(self.hi - self.lo + float("-inf"))