"""A code academy project to write a partially structured madlib that can go offrails based on user input"""

print("Let the MadLibs Begin")

user = input("Please tell us your name: ")
main_char = input("Now " + user + ", give us a name for the main character ... please: ")

print("\n\nGreat. Next we need three adjectives. Anything will do. Make them funny.")
adj1 = input("Tell us the first one " + user + ": ")
adj2 = input("Now the second: ")
adj3 = input("And finally, the third: ")

print("\n\nOK. Just a little more. We need three funny verbs or verbish phrases.")
verb1 = input("So, what's the first verb: ")
verb2 = input("And another: ")
verb3 = input("OK, we're finally there " + user + ". What's the last one: ")

print("\n\nWe now need a few nouns. Four to be exact.")
noun1 = input("And the first is: ")
noun2 = input("The second: ")
noun3 = input("The third: ")
noun4 = input("The last noun is: ")

print("\n\nWe're almost done. We need a few more words or phrases from you.")
animal = input("What's your favourite animal: ")
food = input("Burger or fried chicken? ")
if food.lower() == "burger" or food.lower() == "fried chicken":
    print("A " + food + " lover")
else:
    food = input("Try again. Burger or fried chicken: ")
fruit = input("\n\nName a red fruit: ")
number = input("What is your favourite number: ")
superhero = input("Name a superhero who can fly: ")
country = input("In what country were you born?: ")
dessert = input("Tell me your favourite dessert: ")
year = input("In what year was your father born?: ")

# The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rhythm of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %s ruled the world."

print("\n\n\n" + STORY % (adj1, user, verb1, adj2, noun1, noun2, animal, food, verb2, noun3, fruit, adj3, user, verb3, number, user, superhero,
superhero, user, country, user, dessert, user, year, noun4))
