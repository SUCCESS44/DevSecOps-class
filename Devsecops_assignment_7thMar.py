import random

def all_the_snacks(snack):
    """Prints our snack 100 times"""
    print(snack * 100)
def all_the_snacks_modified(snack, spacer):
    """Prints our snack 100 times"""
    print((snack + spacer) * 100)
def all_the_snacks_modified_again(snack, spacer, num):
    """Prints our snack 100 times"""
    print((snack + spacer) * num)
def price_matcher():
    grocery_list = ["cookies", "ice cream", "peanuts", "chocolate", "ACV", "popcorn"]
    print(random.choice(grocery_list))
def in_grocery_list(lst):
    """checks if an item is in our grocery list"""
    grocery_list = ["cookies", "ice cream", "peanuts", "chocolate", "ACV", "popcorn"]
    for i in lst:
        if i in grocery_list:
            print("True")
        else:
            print("False")
def all_the_snacks_modified_again_the_second_time(snack, spacer=",", num=100):
    """Prints our snack 100 times"""
    print((snack + spacer) * num)
def get_favorite_color():
    favorite = input("What is your favorite Color?: ")
    return favorite

    
def april_fools_caller_swapper():
    """swaps my calor for my neighbors"""
    my_name = input("Please enter your name: ")
    my_favorite_color = input("Please enter your favorite color: ")
    neighbors_name = input("Please enter your neighbors name: ")
    neighbors_color = input("Please Enter your neighbors color: ")
    print(
        f"My name is {my_name} and my favorite color is {my_favorite_color}, my neighbors name is {neighbors_name} and their favorie color is {neighbors_color}"
    )
    print(
        f"My name is {my_name} and my favorie color is {neighbors_color}, my neighbors name is {neighbors_name} and their favorite color is {my_favorite_color}"
    )
def shout():
    """shouts the name of the user"""
    name = input("Please enter your name: ")
    print(f"HELLO {name.upper()}")
some_kind_of_food = "cookies"
another_snack = "patato chips"
third_snack = "Ukraine chips"
all_the_snacks(some_kind_of_food)
all_the_snacks(another_snack)
all_the_snacks(third_snack)
grocery_list = ["cookies", "ice cream", "peanuts", "chocolate", "ACV", "popcorn"]
for i in grocery_list:
    all_the_snacks_modified_again(i, " ", 500)
price_matcher()
basket = ["Bread", "ACV", "popcorn", "Garri"]
in_grocery_list(basket)
print(get_favorite_color())
april_fools_caller_swapper()
shout()