from vector import Vector

G=Vector((3,8))
print(G)
X=Vector([7,6,8,2,1])
print(X)
print(X.__sub__(G.values))
print(X.__radd__(9))
