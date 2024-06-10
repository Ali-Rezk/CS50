def main():
    height = int(input("Height: "))
    for i in range(height):
        brick(i)

def brick(n):
    for i in range(n):
        print("#" end" ")

main()
