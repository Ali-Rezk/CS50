from cs50 import get_float


n = get_float("change owned: ")

while n < 0:
    n = get_float("change owned: ")

x = int((n / 0.25))
y = int((n / 0.10 - x * 2.5))
z = int((n / .05 - y * 2.0 - x * 5.0))
v = int((n / 0.01 - z * 5.0 - y * 10.0 - x * 25.0))
i = int((x + y + z + v))

print(f"{i}")
