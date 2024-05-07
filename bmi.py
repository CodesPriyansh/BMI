print("Welcome To The BMI Calculator.")
print("Let's check your Body Mass Index.")

weight = float(input("enter your weight(in kg's):"))
height = float(input("enter your height(in meters):"))

bmi = weight / (height * height)  

if bmi < 19:
    print(f"your bmi is {bmi}, you're underweight.")
elif bmi > 18.5 and bmi < 24.9:
    print(f"your bmi is {bmi}, you're normal weight.")
elif bmi > 25 and bmi < 29.9:
    print(f"your bmi is {bmi}, you're overweight.")
else: 
    print(f"your bmi is {bmi}, you're obese.")
    
