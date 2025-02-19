x = [1,2,3]
y = x.copy()
print("X: ",hex(id(x)))
print("Y: ",hex(id(y)))
x.append(4)
print("X: ",hex(id(x)))
print("Y: ",hex(id(y)))

