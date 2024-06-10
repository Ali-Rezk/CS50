from cs50 import get_int


n = get_int("change owned: ")

while n < 0:
    n = get_int("change owned: ")

x = (n / 25)
y = (n / 10 - x * 2.5)
z = (n / 5 - y * 2 - x * 5)
v = (n / 1 - z * 5 - y * 10 - x * 25)
i = (x + y + z + v)

print(f"{i}")
