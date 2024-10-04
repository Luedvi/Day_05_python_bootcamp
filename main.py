# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password=""
for letter in range(0,nr_letters):  # we can use the 0 alternatively to the +1 method
  random_letter=random.choice(letters)  # we can use the index method or the choice() function
  password+=random_letter
for symbol in range(1,nr_symbols+1):
  password+=random.choice(symbols)  # we can simplify this step avoiding the creation of more variables (e.g.random_letter) for saving memory space
for number in range(1,nr_numbers+1):
  password+=random.choice(numbers)
print("Your password is:",password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_password=[]
for letter in range(nr_letters):  # we can simplify this by eliminating the 0 as the first parameter in the range function
  random_password.append(letters[random.randint(0,51)])#here we use the index method
for symbol in range(0,nr_symbols):
  random_symbol=symbols[random.randint(0,8)]  # again we can avoid this extra step of creating a variable
  random_password.append(random_symbol)
for number in range(0,nr_numbers):
  random_password+=numbers[random.randint(0,9)]  # we can also use the "+" instead of append() in loops to add items to a list
print(random_password)

random.shuffle(random_password)
print(random_password)

final_password=""  # in this step we convert the list to a string
for character in random_password:
  final_password+=character
print("Your ultimate password is:",final_password)
