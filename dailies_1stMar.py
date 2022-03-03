a = 299 #int
b = 90.0 #float
c = "145" # str
d = "\u0CA0_\u0CA0" #str
e = "True" # str
f = True # bool
g = len('sample') #int
h = 100**30 #int
i = 1 >= 1 #bool
k = 30/7 #float
m = 128 << 1 #int
n = bin(255) #str

my_var = 99
my_var += 11
my_var = str(my_var)
my_var *= 2
my_var = len(my_var)
my_var *= 4
my_var == 24

for i in range(1, 11):
    print(i)

for in range(9):
    print(i)

favourite_snacks = "cookies"
print(favourite_snacks * 100)

grocery_price = [9.42, 5.67, 3.25, 13.40, 7.50]
print(max(grocery_price))

grocery_price = [9.42, 5.67, 3.25, 13.40, 7.50]
print(min(grocery_price))

import random
favourite_snacks = 'cookies'
print(random.randint(0, 100) * favourite_snacks)

grocery_price = [9.42, 5.67, 3.25, 13.40, 7.50]
random.choice(grocery_price)

abs(random.choice(grocery_price))

round(abs(random.choice(grocery_price)))

favourite_snacks = "cookies"
count = 0
while count < 50:
    print(favourite_snacks)
    count += 1

count = 1
favourite_snacks = 'cookies'
while count <= 10:
    print(favourite_snacks * count)
    count += 1

import random
if random.choice(grocery_price) < 10:
    customer_price = random.choice(grocery_price)
    if customer_price < 10:
        print('cashier pay customer', 10 - customer_price)
    elif customer_price > 10:
        print('cashier pay customer', customer_price - 10)
    elif customer_price == 10:
        print('cashier tell customer to leave')
    else:
        print('what do you have in mind')










