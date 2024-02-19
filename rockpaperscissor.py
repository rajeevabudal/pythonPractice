import random

r = random.randint(1, 3)
print(r)
u = int(
    input("Enter the number 1 for rock\n, 2 for paper\n, 3 for scissors: "))

if (r == u):
  print("It is a tie")
elif ((r == 1 and u == 2) or (r == 2 and u == 3) or (r == 3 and u == 1)):
  print("You win")
elif ((r == 1 and u == 3) or (r == 2 and u == 1) or (r == 3 and u == 2)):
  print("You lose")
