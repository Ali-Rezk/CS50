def main():
    height = int(input("Height: "))
    for i in range(height):
        brick(i)
        print(" ", end="")
    print()

def brick(n):
    for i in range(n):
        print("#", end="")
    print()



main()
