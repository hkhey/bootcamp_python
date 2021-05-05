class Matrix:
    def __init__(self,data,shape=None):
        if(not isinstance(data, list) and not isinstance(data, tuple)):
            raise ValueError("Error")
        if(isinstance(data, list)):
            for i in range(len(data)):
                if not isinstance(data[i], list):
                  raise ValueError("Error")
            self.data=data
            self.shape=(len(data), len(data[0])) 
        if(isinstance(data, tuple)):
            L=[[0 for i in range(data[1])] for j in range(data[0])]
            self.data=L
            self.shape=data
        if(isinstance(data, list) and isinstance(shape, tuple)):
            for i in range(len(data)):
                if not isinstance(data[i], list) or (len(data),len(data[0]))!=shape:
                    raise ValueError("Error")
            self.data=data
            self.shape=shape
    def __add__(M, N):
        if(M.shape!=N.shape):
            raise ValueError("Error")
        else:
            m,n=M.shape
            for i in range(m):
                for j in range(n):
                    X.data[i][j]=M.data[i][j]+N.data[i][j]
            return X.data
    def __radd__(M,scalar):
        m=M.shape[0]
        n=M.shape[1]
        for i in range(m):
            for j in range(n):
                M.data[i][j]=M.data[i][j]+scalar
        return M.data
    def __sub__(M,N):
        if(M.shape!=N.shape):
            raise ValueError("Error")
        else:
            m,n=M.shape
            for i in range(m):
                for j in range(n):
                    Z.data[i][j]=M.data[i][j]-N.data[i][j]
            return Z.data
    def __rsub__(M, scalar):
        m=M.shape[0]
        n=M.shape[1]
        for i in range(m):
            for j in range(n):
                M.data[i][j]=M.data[i][j]-scalar
        return M.data
    def __truediv__(M,N):
        if(M.shape!=N.shape):
            raise ValueError("Error")
        else:
            m,n=X.shape
            for i in range(m):
                for j in range(n):
                    if N.data[i][j]==0:
                        raise ValueError("Error:Div by 0 not allowed")
                    Z.data[i][j]=M.data[i][j]//N.data[i][j]
            return Z.data
    def __rtruediv__(M, scalar):
        m=M.shape[0]
        n=M.shape[1]
        for i in range(m):
            for j in range(n):
                M.data[i][j]=M.data[i][j]/scalar
        return M.data
    def __mul__(M,N):
        if(M.shape[1]!=N.shape[0]):
            raise ValueError("Error")
        else:
            m,p=M.shape
            n=N.shape[1]
            Z=[[0 for i in range(n)] for j in range(m)]
            for i in range(m):
                for j in range(p):
                    for k in range(n):
                        Z[i][j]+=M.data[i][k]*N.data[k][j]

            return Z
    def __rmul__(self,M):
        m=self.shape[0]
        n=self.shape[1]
        if n!=len(M):
            raise ValueError("Error")
        Z=[0 for i in range(m)]
        for i in range(m):
            c=0
            for j in range(n):
                c+=self.data[i][j]*M[j]
            Z[i]=c
        return Z
    def __str__(self):
        return "(Matrix : {} Shape : {})".format(self.data, self.shape)
    def __repr__(self):
        rep = f'Matrix(Values: {self.values}, Size: {self.size})'
        return rep
X=Matrix([[1, 2, 3],[3,4,5],[1, 2, 3]])
Z=[1,2,3]
M=X.__rmul__(Z)
print(M) 
