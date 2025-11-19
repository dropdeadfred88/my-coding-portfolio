print("Tip Calculator")

bill = float(input("Total bill amount? $"))
people = int(input("How many people? "))
tip_percent = int(input("What tip % do you want to give? (10, 12, 15) "))

tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount
each = total / people

print(f"Each person should pay: ${each:.2f}")
