height = float(input("what is your height? "))
weight = int(input("what is your weight? "))

bmi = weight / (height * height)

if bmi < 18.5:
  print(f"your bmi is {bmi},you are underweight!")
elif bmi < 25:
  print(f"your bmi is {bmi}, you have a normal weight!")
elif bmi < 30:
  print(f"your bmi is {bmi}, you are selightly overweight!")
elif bmi < 35:
  print(f"your bmi is {bmi}, you are obese!")
else:
  print(f"your bmi is {bmi}, you are clinically overweight!")


