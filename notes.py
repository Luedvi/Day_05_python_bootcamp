animals=["elephant","donkey","mouse","caterpillar","lion","zebra"]
groceries=["eggs","milk","cereal"]
#for loop assigns a temporary variable name(in this case "animal") to the items of the list "animals" and execute the actions in the indented code block over and over until it finishes with the list's items. it's a good practice to name the variable as the singular form of the items in the list
for animal in animals:
  print(animal+animal)
  print(animal+" is beautiful")
  
print("this piece of code is not indented")#when we see a colon ":" in a conditional or loop, the indentation is very important for our code to run exactly as we want

for food in groceries:
  print(food)

# we can have nested loops
map = [[1,2,3,4,5],
       [6,7,8,9,10],
       [11,12,13,14,15],
       [16,17,18,19,20]]

for row in map:
    print(row)
    for column in row:
        print(column)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#sum() function calculates the sum of values passed in the form of list, tuple or dictionary. the second parameter is the initial value with which the addition is going to take place. By default, the start value is set to 0.
number_list=[3,5,7,9,11]
total=sum(number_list)
print(total)

altered_total=sum(number_list,2)
print(altered_total)

#max () function gives the highest value of a given list
max_number=max(number_list)
print(max_number)

rango = range(10)
print(max(rango))

# when used on strings the min() and max() functions follow the lexicographic order
tupla = ('Hola', 'Adiós', 'Buenos días')
print(max(tupla), min(tupla))

#min() function gives the lowest value of a given list
min_number=min(number_list)
print(min_number)

#range () function gives a range for the loop
for number in range(1,10):#it doesn't include the second value, in this case the 10
  print(number)
for number in range(0,4):
  print(number)
for number in range(4):#when it starts at 0 it can be abbreviated with just the second parameter value
  print(number)
# the default step value is also 0 but can be added another value
for number in range(1,24,3):
  print(number)
# we can set the temporary variable to "_" underscore if we won't actually use it
for _ in range(4):
    print("i don't need the temporary variable")
#we can set it to go backwards
for number in range(50,15,-1):
    print(number)

sum_number=0
for number in range(1,101):
  sum_number+=number
print(sum_number)

# we can create a range object that has its own set of attributes
r = range(1, 10, 2)
print(r.start, r.stop, r.step)

# also we can create lists and tuples with range
fluber = list(range(10))
print(fluber)
wozack = tuple(range(5))
print(wozack)

#shuffle () function mixes the items on a given list
import random
print(number_list)

random.shuffle(number_list)
print(number_list)
#we can use a for loop to shuffle as well but takes more steps like the creation of a new list and using the index
lista=["a","b","c","d","e"]
orden=[4,1,3,0,2]
lista1=[lista[o] for o in orden]
print(lista1)
#You can also use for/in to work on a string. The string acts like a list of its chars
city="guadalajara"
for character in city:
    print(character)

#https://docs.python.org/3/library/functions.html#sum
# https://www.w3schools.com/python/python_for_loops.asp
