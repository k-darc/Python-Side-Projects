import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_volume(radius, height):
    base_area = calculate_area(radius)
    return base_area * height

def main():
    try:
        radius = float(input("Enter the Radius of the cylinder: "))
        height = float(input("Enter the Height of the cylinder: "))

        if radius <= 0 or height <= 0:
            raise ValueError("Radius and Height must be valid numbers")

        area = calculate_area(radius)
        volume = calculate_volume(radius, height)

        print("The area of the cylinder is: {area:.2f}")
        print(f"The volume of the cylinder is: {volume:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
