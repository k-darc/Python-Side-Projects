import math

def calculate(rad):
    return math.pi * rad ** 2

def calculate_volume(rad,hgt):
    base = calculate_area(rad)
    return base * hgt

def main():
    rad = float(input("Enter the Radius: "))
    hgt = float(input("Enter the Height: "))



