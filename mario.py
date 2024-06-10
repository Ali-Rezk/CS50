def main():
    height = int(input("Height: "))

    if height < 1:
        

    for i in range(height):
        spaces(height - i - 1)
        bricks(i + 1)
        print("  ", end="")
        bricks(i + 1)
        print()


def bricks(n):
    for i in range(n):
        print("#", end="")


def spaces(n):
    for i in range(n):
        print(" ", end="")


main()
