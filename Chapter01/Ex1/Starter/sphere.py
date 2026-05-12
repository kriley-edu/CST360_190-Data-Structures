# Write your code below:
import math

def main():
radius = float(input("Enter the radius of the sphere: "))
diameter = radius * 2
circumference = 2 * math.pi *radius
surface_area = 4 * math.pi * radius ** 2
volume = (4 / 3) * math.pi * radius ** 3

print("The diameter is ", diameter)
print("The circumference is ", circumference)
print("The surface area is ", surface_area)
print("The volume is ", volume)

if __name__ == "__main__":
    main() 
