import random

# set balance for testing purposes
balance = 5

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