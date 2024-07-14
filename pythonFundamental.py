# age = 89
# height = 10.5
# width = "100"
# depth = "3.9"

# # depth = int (depth)

# width = int(width)
# print(type(age))
# print(type(width))
# print("Depth: "+depth)
# print("Width: "+str(width))
# y = input("What is your name: ")
# a = int(input("How old are you: "))
# # h = input(float("What is your Average height: "))

# print("My name is "+y)
# print("I am "+str(a)+" years old")
# #print("I am an Average height of"+str(h))

# import math
# a = math.pi
# a = -a
# print(abs(a))

# mark = float(input("Enter your marks: "))
# if 90 <= mark <=100:
#     print("Excellent")
# elif 80<= mark <= 89:
#     print("Very Good")
# elif 70 <= mark <= 79:
#     print("Good")
# else:
#     print("Failed")
# for i in range(1,100):
#     if i % 3 == 0 and i % 5 ==0:
#         print("FussBuzz")
#     elif i % 3 == 0:
#         print("Fuss")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print("$")

temp = int(input("What is the Temperature: "))

# if 0 <= temp >=30:
#     print("the temperature is good today")
#     print("go outside")

# elif 0 > temp >30:
#     print("the temperature is very bad")

# else:
#     print("okay")
if temp > 80 and temp < 100:
    print("80 to 100")

elif temp < 80 or temp > 0 :
    print("")