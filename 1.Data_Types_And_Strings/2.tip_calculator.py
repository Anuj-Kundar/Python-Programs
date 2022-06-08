print("Welcome to Tip Calculator!")
bill = int(input("What was the total bill? ₹"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip/100
total_tip = bill*tip_as_percent
total_bill = bill+total_tip
bill_per_person = bill/people

final_amount = round(bill_per_person, 2)

split_bill = print(f"Each person should pay: {final_amount}")
