def main():
    height = int(input("Height: "))
    for i in range(height):
        bricks(height-i)
        print(" ", end="")
        bricks(i)

    print()

def bricks(n):
    for i in range(n):
        print("#", end="")
    print()

def revbricks(n):
    for i in range(n)


main()