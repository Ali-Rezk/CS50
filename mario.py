def main():
    height = int(input("Height: "))
    for i in range(height):
        brick(i)
    print()
    
def brick(n):
    for i in range(n):
        print("#", end="")

main()
