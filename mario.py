def main():
    height = int(input("Height: "))
    for i in range(height):
        spaces(height-i)
        bricks(i)
        print(" ", end="")
        bricks(i)
        print()

def bricks(n):
    for i in range(n):
        print("#", end="")

def spaces(n):
    for i in range(n):
        print(" ", end="")


main()
