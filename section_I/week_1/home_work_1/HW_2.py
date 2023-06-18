#¬(¬p ∧ q)↔(p∨¬q)

p=True
q= True

sol = not((not p and q) and (p or not q)) or not(not q or p) or p or not q

print(p, q, sol, sep=" | ")

p = True
q= False

sol = not((not p and q) and (p or not q)) or not(not q or p) or p or not q

print(p, q, sol, sep=" | ")

p = False
q = True

sol = not((not p and q) and (p or not q)) or not(not q or p) or p or not q

print(p, q, sol, sep=" | ")

p = False
q = False

sol = not((not p and q) and (p or not q)) or not(not q or p) or p or not q

print(p, q, sol, sep=" | ")