doors = [False] * 101

# print(doors)

# for i in range(1, 101):
#     doors[i] = not doors[i]

# print(doors)

# for i in range(1, 6):
#     for j in range(1, 4):
#         print("i:", i, "j:", j)


# Solution
# for i in range(1, 101):
#     for j in range(i, 101, i):
#         doors[j] = not doors[j]

# for i in range(1, 101):
#     if doors[i] is True:
#         print(i, end=", ")


doors = [False] * 11  # So we can start at door 1. We will ignore index 0

for i in range(1, 11):
    # For the second pass, i = 2, so we start at door 2, for the 3rd pass we start at door 3 etc.
    for j in range(i, 11, i):
        print(f"i: {i}; j:{j}; step size: {i}. Toggling door number {j}.")
        doors[j] = not doors[j]  # Using `not` to invert the Boolean value

# Print out just the positions of the open doors
print("Algorithm has finished.")
for i in range(1, 11):
    if doors[i] is True:  # Or just if doors[i]:
        print(f"Door number {i} remains open.")