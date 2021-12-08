number = 0

while number < 10:
  number = number + 1
  print(number)

# Additional solution:

number = 1
while number < 11:
    print(number)
    number = number + 1

# You can print the number first, or add one to the number first, it doesn't matter-
# as long as the logic in your while loop conditional matches the order you are doing the steps within it

# For example, the follow solution would be incorrect:
number = 1
while number < 10:
    number = number + 1
    print(number)
# As this would give us a program that counts from 2-11
