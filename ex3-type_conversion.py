# age calculator

from datetime import date

current_date = date.today()

current_year = current_date.year

birth_year = input("what year you were born? \n")

age = current_year - int(birth_year)

print(f"your age is {age}")
