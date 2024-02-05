# Week3 Class: Comprehensions
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

#######################################################
## List Comprehension
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

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]


#######################################################
## Dictionary Comprehension
#   { <expression> for x in <sequence> if <condition> } 

# Using one input list
numdict = { x:x**2 for x in number }
print("Using one input list to create dict: ", numdict)

# Using two input list
months_dict = { key:value for (key, value) in zip(number, months) }
print("Using two lists: ", months_dict)

#######################################################
## Set Comprehension
#   { <expression> for x in <sequence> if <condition> } 

# Set Comprehension is very similar to List Comprehension exception using curly brackets instead of square brackets 
# Set member is unique instead of Dictionary's allowing duplication
set_a = { x for x in range(10, 20) if x not in [12, 14, 16] }
print(set_a)


#######################################################
## Generator Comprehension
#   ( <expression> for x in <sequence> if <condition> ) 
data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = ( x for x in data )
print(gen_obj)
print(type(gen_obj))
for x in gen_obj:
    print(x, end=" ")



