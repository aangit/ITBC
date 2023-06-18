# ((p→r)∧(q→r))↔((p∨q)→r))

p = False
q = False
r = False

sol = ((not p or r) and (not q or r) and (not(p or q) or r)) or not (
    (not p or q) and (not q or r) or (not(p or q) or r))
print(p, q, r, sol, sep=" | ")

p = False
q = False
r = True

sol = ((not p or r) and (not q or r) and (not(p or q) or r)) or not (
    (not p or q) and (not q or r) or (not(p or q) or r))
print(p, q, r, sol, sep=" | ")

p = False
q = True
r = False

sol = ((not p or r) and (not q or r) and (not(p or q) or r)) or not (
    (not p or q) and (not q or r) or (not(p or q) or r))
print(p, q, r, sol, sep=" | ")


p = False
q = True
r = True

sol = ((not p or r) and (not q or r) and (not(p or q) or r)) or not (
    (not p or q) and (not q or r) or (not(p or q) or r))
print(p, q, r, sol, sep=" | ")

p = True
q = False
r = False

sol = ((not p or r) and (not q or r) and (not(p or q) or r)) or not (
    (not p or q) and (not q or r) or (not(p or q) or r))
print(p, q, r, sol, sep=" | ")

p = True
q = False
r = True

sol = ((not p or r) and (not q or r) and (not(p or q) or r)) or not (
    (not p or q) and (not q or r) or (not(p or q) or r))
print(p, q, r, sol, sep=" | ")

p = True
q = True
r = False

sol = ((not p or r) and (not q or r) and (not(p or q) or r)) or not (
    (not p or q) and (not q or r) or (not(p or q) or r))
print(p, q, r, sol, sep=" | ")

p = True
q = True
r = True

sol = ((not p or r) and (not q or r) and (not(p or q) or r)) or not (
    (not p or q) and (not q or r) or (not(p or q) or r))
print(p, q, r, sol, sep=" | ")