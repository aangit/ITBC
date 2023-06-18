#p→(p∨q)

p = True
q = True

sol = not p or (p or q)
print(p, q, sol, sep= " | ")

p = True
q = False

sol = not p or (p or q)
print(p, q, sol, sep= " | ")

p = False
q = True

sol = not p or (p or q)
print(p, q, sol, sep= " | ")

p = False
q = False

sol = not p or (p or q)
print(p, q, sol, sep= " | ")
