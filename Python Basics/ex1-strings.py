name = "Johnny"
age = 30

print("Hello, " + name + ". You are " + str(age) + " years old")  # Concatenation
print(f"Hello, {name}. You are {age} years old")  # f-string formatting
print("Hi {}. You are {} years old".format(name, age))

# we need to put in the brackets new_name, and age if we create them in .format
print("Hi {new_name}. You are {age} years old".format(new_name="Sally", age=100))

# string indexes, str is an order seq of characteres
# Guess the output of each print statement before you click RUN!
python = "I am PYHTON"
# [start:stop]

print(python[1:4])  # am
print(python[1:])  # am PYHTON
print(python[:])  # I am PYHTON
print(python[1:100])  # am PYHTON
print(python[-1])  # N
print(python[-4])  # H
print(python[:-3])  # I am PYH
print(python[-3:])  # TON
print(python[::-1])  # NOTHYP ma I
