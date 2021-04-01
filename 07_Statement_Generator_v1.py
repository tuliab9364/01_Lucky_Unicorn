def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    
    print (top_bottom)
    print (greeting)
    print (top_bottom)

    return ""

# Main routine goes here
statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()
statement_generator("Congratulation you got a Unicorn", "!")