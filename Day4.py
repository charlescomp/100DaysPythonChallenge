import random

# Random number between 0 and 1
random_number = random.random()
print(f"Random number between 0 and 1: {random_number}")

# Random integer between 1 and 10
random_int = random.randint(1, 10)
print(f"Random integer between 1 and 10: {random_int}")

# Random choice from a list
choices = ["apple", "banana", "cherry"]
random_choice = random.choice(choices)
print(f"Random choice from list: {random_choice}")

# Shuffle a list
deck = [1, 2, 3, 4, 5]
random.shuffle(deck)
print(f"Shuffled deck: {deck}")
