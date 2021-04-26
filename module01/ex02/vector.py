class Vector:
    def __init__(self,arg):
        if isinstance(arg, int):
            self.values = [float(i) for i in range(0, arg)]
        if isinstance(arg, list):
            self.values = arg
        if isinstance(arg, tuple):
            self.values = [float(i) for i in range(arg[0], arg[1])]
        self.size = len(self.values)
    def __add__(self,L):
        if(self.size==len(L)):
            for i in range(self.size):
                self.values[i]+=L[i]
            return self.values
        else:
            return "Size error"
    def __radd__(self,scalar):
        for i in range(self.size):
            self.values[i]+=scalar
        return self.values
    def __sub__(self,L):
        if(self.size==len(L)):
            for i in range(self.size):
                self.values[i]-=L[i]
            return self.values
        else:
            return "Size error"
    def __rsub__(self,scalar):
        for i in range(self.size):
            self.values[i]-=scalar
        return self.values
    def __truediv__(self,L):
        if(self.size==len(L)):
            for i in range(self.size):
                self.values[i]//=L[i]
            return self.values
        else:
            return "Size error"
    def __rtruediv__(self,scalar):
        for i in range(self.size):
            self.values[i]//=scalar
        return self.values
    def __multi__(self,L):
        if(self.size==len(L)):
            for i in range(self.size):
                self.values[i]*=L[i]
            return self.values
        else:
            return "Size error"
    def __rmulti__(self,scalar):
        for i in range(self.size):
            self.values[i]*=scalar
        return self.values
    def __str__(self):
        return f"Vector({self.values})"
    def __repr__(self):
        repr = f'Vector(Values: {self.values}, Size: {self.size})'
        return repr
