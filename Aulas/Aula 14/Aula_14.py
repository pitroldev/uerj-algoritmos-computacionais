# UERJ - 24/11/2020
# Aula 14 de Algoritmos Computacionais

from collections import deque

d = deque('ghi')

for element in d:
    print(element.upper())

d.append("j")
d.appendleft("f")

print(d)

d.pop()
d.popleft()

print(list(d))
print(d[0])
print(d[-1])
