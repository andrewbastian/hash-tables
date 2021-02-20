# Your code here
with open('robin.txt') as file:
    robin = file.read()

from collections import defaultdict

# import matplotlib.pyplot as plt

def histo(s):
    ignore = ',":;,.-+=/\\|[]{}()*^&'
    counter = defaultdict(int)

    clean_up = s.translate(str.maketrans('','', ignore))

    for i in clean_up.lower().split():
        counter[i] += 1

    lst = list(counter.items())
    lst.sort(key=lambda e: e[1], reverse=True)

    biggest_count = sorted(counter.key(), key=lambda j: len(j)[-1])

    for k, v in lst:
        print(f'{' ' * (biggest_count - len(k)) + v * '#'}')

histo(robin)