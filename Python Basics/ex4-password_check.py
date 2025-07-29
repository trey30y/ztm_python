# password checker
# username = input("username: ")
# password = input("password: ")

# password_hash = "*" * len(password)
# print(f"{username}, your password {password_hash} is {len(password_hash)} long")


def replace_all_chars(s, replacement_char):
    return replacement_char * len(s)


username = input("username: ")
password = input("password: ")

password_hash = password.replace(password, replace_all_chars(password, "*"))
print(
    f"{username}, your password {password_hash} is {len(password_hash)} characters long"
)
