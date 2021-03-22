

# Function go here...
def yes_no(question):...


def instruction():...

def num_check(question, low, high):...


# Main Routine goes here...
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instruction()

print("Program continues")

# Ask user how much they want to play with...
how_much = num_check("How much would you like to play?", 0, 10 )

print("You will be spending ${}".format(how_much))
