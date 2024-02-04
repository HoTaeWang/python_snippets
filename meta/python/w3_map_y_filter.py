# Week3 Class: map / filter
menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

def select_menu(menu_name):
    if menu_name[0] == 'c':
        return menu_name

# map ==> return all 
filtered_menu = map(select_menu, menu)
print(filtered_menu)
for x in filtered_menu:
    print(x)

filtered = filter(select_menu, menu)
print(filtered)
for x in filtered:
    print(x)


