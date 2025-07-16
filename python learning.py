import itertools
"""counter = itertools.count(10)

for i in counter:
    print(i)
    if i == 20:
        break"""

list =["A", "B", "C"]
cycler = itertools.cycle(list)
for i, letter in enumerate(cycler):
    print(i, letter, sep=": ")
    if i == 20:
        break