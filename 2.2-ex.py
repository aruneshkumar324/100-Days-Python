# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# print(type(height))

# BMI = weight / (height * height)
BMI = weight / height ** 2

# print(BMI)
print(int(BMI))
