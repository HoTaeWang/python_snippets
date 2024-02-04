# Week3 Class: Comprehensions
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# List Comprehension
#   [ <expression> for x in <sequence> if <condition> ]

# Ex1: List Comprehension: Updating the same list
data = [x+3 for x in data]
print("Updating the list: ", data)

# Ex2: List Comprehension: Creating a different list with updated value
new_data = [x*2 for x in data]
print("Creating new list: ", new_data)

# Ex3: List Comprehension, With an if-condition : Multiples of four
fourx = [x for x in new_data if x%4 == 0]
print("Divisible by four: ", fourx)

# Ex4: Alternately, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x%4 == 0]
print("Divisible by four minus one: ", fourxsub)

# Ex5: List Comprehension, Using range function
nines = [x for x in range(100) if x%9 == 0]
print("Nines : ", nines)



