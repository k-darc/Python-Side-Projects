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
