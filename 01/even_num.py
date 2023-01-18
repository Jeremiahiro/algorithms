# Print even numbers

# Solution 1
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i)

# Solution 2 - using step parameter of the range function (Brute Force Algorithm) 
for i in range(2, 101, 2):
    print(i)