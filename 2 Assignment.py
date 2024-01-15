# 111111111111111111111111111111111111

string = "Hello Python"


def remover(string):
    result = ""
    for char in string:
        if char not in result:
            result += char
    return result


print(remover(string))

# 222222222222222222222222222222222222

mystr = "He12llo, Py00th55on!"


def noNumbers(string):
    result = ""
    for char in string:
        if char not in "0123456789":
            result += char
    return result


print(noNumbers(mystr))

# 33333333333333333333333333333333333


def numberTree():
    n = 6

    for i in range(1, n):
        print((str(i) + " ") * i)


numberTree()

# 44444444444444444444444444444444444

string1 = "madam"


def uniqueChar(string1):
    r = ""
    for i in string1:
        if i not in r:
            r += i
    print(len(r))


uniqueChar(string1)

# 555555555555555555555555555555555555

numbers_x = [11, 20, 30, 40, 11]
numbers_y = [25, 65, 35, 75, 30]


def listCheck(list):
    if list[0] == list[-1]:
        return True
    else:
        return False


print(listCheck(numbers_x))
print(listCheck(numbers_y))

# 66666666666666666666666666666666666

numbers_z = [242, 23, 55, 101, 112]


def palindrome(list):
    for i in range(len(list)):
        if list[i] == int(str(list[i])[::-1]):
            print(f"{list[i]} is a palindrome.")
        else:
            print(f"{list[i]} is not a palindrome.")


palindrome(numbers_z)

# 7777777777777777777777777777777777777

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]


def filter_odds_evens(only_odds, only_evens):
    list_odds = []
    for num in only_odds:
        if num % 2 != 0:
            list_odds.append(num)

    list_evens = []
    for num in only_evens:
        if num % 2 == 0:
            list_evens.append(num)

    result_list = list_odds + list_evens

    return result_list


print("Result list:", filter_odds_evens(list1, list2))
