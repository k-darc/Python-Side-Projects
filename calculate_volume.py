import math

def calculate(radius):
    return math.pi * radius ** 2

def calculate_volume(radius, height):
    base = calculate_area(radius)
    return base * height

def main():
    radius = float(input("Enter the Radius: "))
    height = float(input("Enter the Height: "))



