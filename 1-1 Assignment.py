stars = "* "
space = " "
tree = ""
spaces = ""
x = 5
for i in range(x):
    tree = tree + stars
    spaces = (space * (x - 1))[i::]
    print(spaces + tree)


n = int(input("Give me a Number to sum: "))
t = 0
for i in range(n + 1):
    t = t + i
    print(t)

text = input("Write a string: ")
even = text[::2]
list1 = list(even)
print(list1)
