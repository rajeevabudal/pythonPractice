weight = int(input("Enter the weight: "));
height = float(input("Enter the height: "));

bmi = weight / (height * height);
print(bmi)
if bmi > 30:
    print("You are obbese");
elif bmi<30 and bmi >25:
    print("You are overweight");
elif bmi<25 and bmi>18.5:
    print("Normal weight");
else:
    print("You are under weight");
