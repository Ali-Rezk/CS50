from cs50 import get_float


n = get_float("change owned: ")

while n < 0:
    n = get_float("change owned: ")

int x = (n / 0.25)
int y = (n / 0.10 - x * 0.25)
int z = (n / 0.5 - y * 0.2 - x * 0.5)
int v = (n / 0.1 - z * 0.5 - y * 0.1 - x * 0.25)
int i = (x + y + z + v)

print(f"{i}")
