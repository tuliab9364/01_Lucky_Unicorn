# Functions go here . . .
def yes_no (question):
  valid = False
  while not valid :

        response = input(question).lower () 

        if response == "yes" or response == "y":
          return("yes")

        elif response == "no" or response == "n":
          return("no")
        else:
          print("Please answer yes/no")    

# Main Routine goes here...
show_instruction = yes_no("Have you played the game before? ")
print("You said {}".format(show_instruction))