import random

name = ['a', 'b', 'c', 'd']
ang = ['1', '2', '3', '4']
char = ['!', '@', '#', '$']
word = []

with open('pass.txt', 'r') as fr:
  word = [w for w in fr.read().split() if len(w) > 5]

pass_humanity = random.choice(word) + ''.join(random.choices(
    ang, k=2)) + ''.join(random.choices(char, k=2))

print(pass_humanity)

# print(random.choices(name, k=3))
# print(random.choice(name) + random.choice(ang) + random.choice(char))
