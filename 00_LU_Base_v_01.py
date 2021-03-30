import random

# Function go here...
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


def instructions():
    print("**** How to play ****")
    print()
    print("The rules of the game here")
    print()
    return ""

def num_check(question, low, high):
  error = "Please enter an whole number between 1 and 10\n"

  valid = False
  while not valid:
    try:
      # ask the question
      response = int (input(question))
      # if the amount is too low / too high give 
      if low < response <= high:
            return response


      # output an error
      else:
        print(error)

    except ValueError:
      print(error)

def statement_generator(statement, decoration):...
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = "*" * len (greeting)

print(top_bottom)
print(greeting)
print(top_bottom)


# Main Routine goes here...
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
  instructions()

else:
  print("Program continues")

# Ask user how much they want to play with...
how_much = num_check("How much would you like to play?", 0, 10 )

balance = how_much

rounds_played = 0

play_again = input("Press <Entre> to play...").lower()
while play_again == "":

    # increase # of rounds rounds_played
    rounds_played += 1

    #Print round number
    print("*** Round #{} ***". format(rounds_played))
    
    chosen_num = random.randint(1,100)

    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4

    # if the random # is between 6 and 36
    # user gets donkey (subtract $1 from the balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1

    # The token is either a horse or zebra...
    # in both cases, subtract $0.50 from the balance
    else:
          # if the is even, set the chosen
          # item to a horse
          if chosen_num % 2 == 0:
            chosen = "horse"

                # otherwise set it to a zebra
          else:
                chosen = "zebra"
          
          # take 50c of balance for horse OR zebra      
          balance -= 0.5


    print("You got a {}, you have ${:.2f} left".format(chosen, balance))
    print()

    if balance < 1:
        play_again = "xxx"
        print("sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit")

print()
print("Final balance", balance)
