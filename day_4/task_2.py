import random

list_item = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

list_item[0] = "kiwi"

list_item.append("grapes")

print(list_item)

# choice 1
random_fruit = random.choice(list_item)
print(random_fruit)

# choice 2
random_fruit2 = random.randint(0, len(list_item) - 1)
print(list_item[random_fruit2])

