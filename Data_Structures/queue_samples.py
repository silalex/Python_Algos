# double-ended queue -> 'deque'
from collections import deque

# 1: Left-2-Right Queue
queue = deque(['orange', 'apple', 'pear', 'banana'])
print("#1 (Left-2-Right Queue):")
print(queue)

queue.append('kiwi')
print(queue)

queue.popleft()
print(queue)
print()

# 2: Right-2-Left Queue
queue = deque(['orange', 'apple', 'pear', 'banana'])
print("#2 (Right-2-Left Queue):")
print(queue)

queue.appendleft('kiwi')
print(queue)

queue.pop()
print(queue)

