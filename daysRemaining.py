age = input("Please enter your age? ")
age_as_int = int(age);

yearsRemaining = 90-age_as_int;
daysRemaining = yearsRemaining * 365;
weeksRemaining =  yearsRemaining * 52;
monthsRemaining = yearsRemaining * 12;
print(f"You have {daysRemaining} days, {weeksRemaining} weeks , and {monthsRemaining} months remaining until the age of 90")
