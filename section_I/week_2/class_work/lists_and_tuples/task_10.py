# Split the given string so that every character of the string except space becomes an element of a tuple. Show tuples.
# String: "I'm watching football and crying."

word = "I am watching football and crying."

list_1 = []
for i in word:
    if i != " ":
        list_1.append(i)

t = tuple(list_1)
print(t)