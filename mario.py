def main():
    height = int(input("Height: "))
    for i in height:
        brick(i)

def brick(n):
    for i in rang(n):
        print("#")

main()
