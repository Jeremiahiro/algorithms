# Print fizzbuzz if the number is divisible by 3 and 5;
# print fizz if the number is divisible by 3
# print buzz if the number is divisible by 5

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

# The `%` operator gives the remainder of the left-hand value when divided by the right-hand value.
