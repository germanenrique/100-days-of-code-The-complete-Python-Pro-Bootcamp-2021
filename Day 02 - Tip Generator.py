print("Welcome to day 2 - Project: Tip Calculator. Lets go!\n")

total_bill = float(input("What was total bill? "))
percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
total_people = float(input("How many people to split the bill "))
percentage2 = percentage / 100
total_bill = total_bill + total_bill * percentage2

total_bill = total_bill / total_people

message = (round(total_bill,2))

print("They must pay " + str(message))