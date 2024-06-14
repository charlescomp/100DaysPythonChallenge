# Control Flow and Logical Operators

# if-elif-else statement
temperature = 25

if temperature > 30:
    print("It's a hot day.")
elif temperature > 20:
    print("It's a warm day.")
else:
    print("It's a cold day.")

# Logical operators
is_raining = False
is_sunny = True

if is_raining and is_sunny:
    print("Look, a rainbow!")
elif is_raining and not is_sunny:
    print("Take an umbrella.")
elif not is_raining and is_sunny:
    print("It's a nice day.")
else:
    print("The weather is unclear.")

# for loop
for i in range(5):
    print(f"Iteration {i}")

# while loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1
