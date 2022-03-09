
#question1
list = (9.42, 5.67, 3.25, 13.40, 7.50)
for i in list:
    if i < 10:
        print('True')
    else:
        print('False')

#question2
list = ['bread', 'butter', 'groundnuts', 'sugar', 'garri', 'egusi', 'ogboono', 'eru']
listB = ['bread', 'rice', 'okra', 'water', 'egusi']
if (all(i in list for i in listB)):
    print("True")
else:
    print("False")    

#question3
phrase = "Blood-oxygenation level dependent functional magnetic resource imaging"
for i in phrase:
    print(i,end ="")

#question4
grocery_list = ['apple','egg','peas','candy','orange']
for i in grocery_list:
    print("Note to self, buy", i)

for i, item in enumerate(grocery_list, 1):
    print(i, "" + item, sep = " ")

favourite_snack = "candy"
for i in grocery_list:
    if i == favourite_snack:
        print(i)
        break

i = phrase.split()
print(i)


for i, item in enumerate(grocery_list, 1):
    print(i ," " + item, sep = "")