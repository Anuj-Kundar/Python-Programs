# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 monthss old
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
real_age=int(age)
real_age=90-real_age
days=real_age*365           #Calculates Days Remaining
weeks=real_age*52           #Calculates Weeks Remaining
months=real_age*12          #Calculates Months Remaining
print(f"You have {days} days, {weeks} weeks and {months} months left")