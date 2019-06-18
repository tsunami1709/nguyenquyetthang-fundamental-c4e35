print("BMI Program")
height_cm = float(input("Your height (cm): "))
weight_kg = float(input("Your weight (kg): "))
height_m = height_cm/100
BMI = weight_kg / (height_m*height_m)

print("You: ", end="")

if BMI <= 16:
    print("Severely underweight")
elif 16 < BMI <= 18.5:
    print(Underweight)
elif 18.5 < BMI <= 25:
    print("Normal")
elif 25 < BMI <= 30:
    print("Overweight")
else:
    print("Obese")
 