def my_sum(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total


my_list = [5, 4, 3, 2, 1]
print(my_sum(my_list))


# The longer the list, the longer the new list that get’s returned. Thus, space increases and the list increases.
def double(lst):
    new_list = []
    for i in range(len(lst)):
        new_list.append(lst[i] * 2)
    return new_list


my_list = [5, 4, 3, 2, 1]
print(double(my_list))