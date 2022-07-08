from random import randint
import random

for i in range(10):
    random.seed(i)
    print(randint(1, 100))