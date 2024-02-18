#Lower and upper
String = "Hello world"

print(String.upper())

print(String.lower())

# ---------------------------------------------------------------------
#Odd sequence

original_sequence = [1, 2, 34, 65, 1, 2, 65, 66, 44, 33, 22, 87, 123412, 9, 78, 76]

odd_sequence = [num for num in original_sequence if num % 2 != 0]

print(odd_sequence)

# --------------------------------------------------------------

fruits = {'apple': 10, 'mango': 20, 'pineapple': 25, 'orange': 30, 'strawberry': 50, 'jackfruit': 10}

fruits_more_than_20 = {key: value for key, value in fruits.items() if value > 20}

print(fruits_more_than_20)

# --------------------------------------------------------------
