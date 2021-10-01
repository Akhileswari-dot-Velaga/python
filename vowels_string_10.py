#Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.


import random
char=['a','e','i','o','u']
for i in range(10):
    random.shuffle(char)
    print(' '.join(char))

