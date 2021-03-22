
try:
  best_num = int(input("What is your favourite number? "))

  print("Your favourite number is", best_num)

except ValueError: 
  print("Oops - you did not enter a number")