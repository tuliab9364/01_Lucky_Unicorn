greeting = "hello world"
sides = "*" * 3

greeting = " {} {} {}".format(sides, greeting, sides)

top_bottom = "*" * len (greeting)

print(top_bottom)
print(greeting)
print(top_bottom)

return ""

# Main routine goes here
statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()
statement_generator("Congratulation you got a Unicorn", "!")