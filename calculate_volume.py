import math

def calculate(radius):
    return math.pi * radius ** 2

def calculate_volume(radius, height):
    base_area = calculate_area(radius)
    return base_area * height

def main():
    try:
        radius = float(input("Enter the Radius: "))
        height = float(input("Enter the Height: "))

        if radius <= 0 or height <= 0:
            raise Value Error("Radius and Height must be valid numbers")

        area = calculate_area(rad)
        volume = calculate_volume(rad, height)