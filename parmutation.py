

'''
A B 

A B
B A 

A B C

A B C
A C B 
B A C
C A B
B C A
C B A

'''
from itertools import permutations
# list = [1, 2, 3]
list = ['I', 'learn', 'python']
for i in permutations(list):
    print(i)