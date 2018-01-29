# Pyglatin translator exercise for Codeacademy

pyg = 'ay'  # suffix variable

original = input('Enter a sinle word - no spaces or special characters:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    print("You entered " + original)
    new_word = word[1:len(word)] + first + pyg  # convert to pyglatin
    print("\nYour pyglatin translation is " + new_word)
else:
    print("Yo dummy, enter a word for us")
