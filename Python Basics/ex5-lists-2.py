# list([iterable])
# iterable (optional): Any iterable (like a string, tuple, list, set, dict, or range).

# If no argument is passed, it returns an empty list.

basket = list(range(1, 5))
# print(f"the length of {basket} is {len(basket)}")

# adding - append changes the list in place, it doesn't produce a value
basket.append(100)
print(basket)  # [1, 2, 3, 4, 100]

# insert - inserts the specified value at the specified position. Insert modifies the list in place
basket.insert(2, 101)
print(basket)  # [1, 2, 101, 3, 4, 100]

# extend - adds the specified list elements(or any iterable) to the end of the current list
basket.extend([200, 201])
print(basket)  # [1, 2, 101, 3, 4, 100, 200, 201]


# removing
# pop - removes the element at the specified position. Returns the value popped
fruits = ["apple", "banana", "cherry", "berry", "tomato"]

popped_fruit = fruits.pop(1)
print(fruits, popped_fruit)  # ['apple', 'cherry', 'berry', 'tomato'] banana

# remove - removes the first occurrence of the element with the specified value. Doesn't return a value
removed_fruit = fruits.remove("berry")
print(fruits)  # ['apple', 'cherry', 'tomato']

# clear - removes all the elements from a list. doesn't return a value
fruits.clear()
print(fruits)  # []

new_basket = ["a", "b", "c", "c", " e"]
# index - returns the position at the first occurence of the specified value
print(f'index of "c" is {new_basket.index("c")}')
print("c" in new_basket)  # True
print("x" in new_basket)  # False

# count - returns the numer of elements with the specified value
print(new_basket.count("c"))  # 2
