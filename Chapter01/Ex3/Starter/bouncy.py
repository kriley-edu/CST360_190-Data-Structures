# Write your code below:
def main():
    height = float(input("Enter initial height: "))
    bounces = int(input("Enter number of bounces: "))
    index = float(input("Enter bounciness index: "))

    down = height
    up = down * index
    total_distance = 0

    for i in range(bounces):
        # Calulate total distance
        total_distance += (down + up)

        # prepare next bounce height
        down = up
        up = down * index        

    print(f"\nTotal distance traveled: {total_distance:.2f} feet")

if __name__ == "__main__":
    main()
