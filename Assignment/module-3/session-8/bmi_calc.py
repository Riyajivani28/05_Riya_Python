import math

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
bmi = weight / math.pow(height, 2)
print("BMI is:", round(bmi, 2))