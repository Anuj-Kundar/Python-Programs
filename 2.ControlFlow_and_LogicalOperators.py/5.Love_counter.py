# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_l=name1.lower()
name2_l=name2.lower()
combined_name=name1_l+name2_l

t=combined_name.count('t')
r=combined_name.count('r')
u=combined_name.count('u')
e=combined_name.count('e')
true =t+r+u+e

l=combined_name.count('l')
o=combined_name.count('o')
v=combined_name.count('v')
e=combined_name.count('e')
love =l+o+v+e

true_score=str(true)+str(love)
love_score=int(true_score)


if((love_score<10) and (love_score>90)):
    print(f"Your love score is {love_score}, you go together like coke and mentos")
if((love_score>40) and (love_score<50)):
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your love score is {love_score}")