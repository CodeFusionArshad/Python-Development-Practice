# #Score Task 1

# bill = float(input("Enter the Total Bill \n"))

# if bill > 5000:
#     discout = bill * 0.20
#     final = bill - discout
#     print("20% dicout is applied : ",final )
# else : print(" Sorry You Are Not Eligible")


# #score task 2
# test_score = float(input("Enter the test score \n"))
# inter_score = float(input("Enter Your Interview Score \n"))

# if test_score>=80 and inter_score>=60:
#     print("Your Are Admited!")
# elif test_score <80:
#     print("You are Failed In Test.")
# elif inter_score <80:
#     print("You are Failed In Interview.")


# # Task 3: Number Categorization

# # Input: Take a number from the user
# number = float(input("Enter a number: "))

# # Check if the number is positive
# if number > 0:
#     # Further check if it's even or odd
#     if number % 2 == 0:
#         print("Positive Even")
#     else:
#         print("Positive Odd")

# # Check if the number is negative
# elif number < 0:
#     # Check if the absolute value is greater than 10
#     if abs(number) > 10:
#         print("Large Negative")
#     else:
#         print("Small Negative")

# # Check if the number is zero
# else:
#     print("Zero")


# task 4 
obt_marks = float(input("Enter Your Obtained Marks"))
total_marks = float(input("Enter Your total marks"))
percentage =obt_marks / total_marks * 1000

if percentage>=900 :
    if percentage>=95:
        print("your grade is A+")
    else:print("your grade is A")

elif percentage >=80:
  if percentage >=85:
      print("Your Grade is B+")
  else:print("your grade is B")

else:print("Your grade is B")