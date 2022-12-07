import random

a = set(random.sample(range(0,1000),50))
b = set(random.sample(range(0,1000),50))

print(f'Первое множество: {a}\n')
print(f'Второе множество: {b}\n')

print(f'Элементы, которые одновременно входят в оба множества: {a.intersection(b)}\n')
print(f'Элементы, которые входят в первое множество, но не входят во второе: {a.difference(b)}\n')
print(f'Элементы, которые входят во второе множество, но не входят в первое: {b.difference(a)}\n')
print(f'Элементы, которые входят в первое или во второе, но не в оба из них одновременно: {b.symmetric_difference(a)}\n')