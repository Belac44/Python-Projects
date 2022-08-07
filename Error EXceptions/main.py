fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError as message:
        print(message)

make_pie(2)
