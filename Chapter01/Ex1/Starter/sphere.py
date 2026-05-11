# Write your code below:
import math

def main():
    radius = float(input("Enter the radius of the sphere: "))

    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    surface_area = 4 * math.pi * radius ** 2
    volume = (4 / 3) * math.pi * radius ** 3

    print(f"\nDiameter: {diameter:.2f}")
    print(f"Circumference: {circumference:.2f}")
    print(f"Surface Area: {surface_area:.2f}")
    print(f"Volume: {volume:.2f}")


if __name__ == "__main__":
    main()
