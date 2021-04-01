# Functions go here
def choice_checker(question):

    error = "Please choose from rock / paper / " \ "scissors (or xxx to quit)"

    valid = False
    while not valid:

        # Ask user for choice
       response = input(question)

       if response == "r" or response == "rock":
            return response
       elif response

# Main routine goes here

# Ask user for choice and check it's valid
user_choice = choice_checker("Choose rock / paper / scissors (r/p/s): ")

# print out choice for comparison purposes
