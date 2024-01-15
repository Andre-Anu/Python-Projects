def add_numbers(a, b):
    return a + b


a = 3
b = 5

print("")
print(f"{a} + {b} = {add_numbers(a, b)}")


# ------------------------------------------#


def perform_operations(a, b):
    s = a + b
    su = a - b
    m = a * b

    return s, su, m


a = 11
b = 7

print("---------------")
s, su, m = perform_operations(a, b)
print(f"{a} + {b} = {s}")
print(f"{a} - {b} = {su}")
print(f"{a} * {b} = {m}")

# ------------------------------------------#


def vowels_consonants(w):
    vowels = "aeiouAEIOU"
    v = 0
    c = 0

    for char in w:
        if char in vowels:
            v += 1
        else:
            c += 1

    return v, c


print("---------------")
w = "BigChumgs"
v, c = vowels_consonants(w)
print(f'"{w}"')
print(f"Vowels: {v}")
print(f"Consonants: {c}")


# ------------------------------------------#


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = 5
print("---------------")
print(f"{n}! = {factorial(n)}")
print("")
