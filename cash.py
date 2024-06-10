from cs50 import get_float


n = get_float("change owned: ")

while n < 0:
    n = get_float("change owned: ")

x = int((n / 0.25))
y = int((n / 0.10 - x * 0.25))
z = int((n / 0.5 - y * 0.2 - x * 0.5))
v = int((n / 0.1 - z * 0.5 - y * 0.1 - x * 0.25))
i = int((x + y + z + v))

print(f"{i}")
