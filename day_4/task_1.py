import random

random_integer = random.randint(1, 10)
print(random_integer)

random_1_to_10 = random.random() * 5
print(random_1_to_10)

random_float = random.uniform(1, 10)
print(random_float)

random_num = random.randint(0,1)

if random_num == 0:
    print("Heads")
else:
    print("Tails")