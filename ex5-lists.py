# lists are an ordered sequence of objects that can be of any type

# the lists are ordered, it means that the items have a defined order, and that order will not change
# if you add new items to a list, the new items will be placed at the end of the list

# What is the output of this code?
# Before you clikc RUN, guess the output of each print statement!
new_list = ["a", "b", "c"]
print(new_list[1])  # b
print(new_list[-2])  # b
print(new_list[1:3])  # ["b", "c"]
new_list[0] = "z"
print(new_list)  # ["z", "b", "c"]

my_list = [1, 2, 3]
bonus = my_list + [5]
my_list[0] = "z"
print(my_list)  # ["z", 2, 3]
print(bonus)  # [1,2,3,5]

# copying a list
copy_list = new_list.copy()
# Avoid copy_list = my_list (this just creates a reference)
#