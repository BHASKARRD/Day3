
print(" Welcome to the Rollercoaster")
height = int(input("what is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("what is your age? "))
  if age <= 12:
    bill = 5
    print("Please pay $7.")
  elif age <= 18:
    bill = 7
    print("Please pay $10.")
  else:
    bill = 12
    print("Please pay $17.")


  wants_photo = input("Do you want a photo taken? y or n")
  if wants_photo == "y":
    bill += 3
    print (f"your final bill is {bill}")
else:
  print("sorry, you have to grow taller before ride")


  



