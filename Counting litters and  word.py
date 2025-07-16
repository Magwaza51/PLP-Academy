quotation = "And we danced, on the brink of an unknow future, to an echo from a vanished past"

# romove punctuation 
import string
ttable = str.maketrans('','',string.punctuation)
clean_quote = quotation.translate(ttable)
print(clean_quote)

print("Number of letters = " + str(len(clean_quote)))

letter_set = set(clean_quote)
print("Number of unique letters = " + str(len(letter_set)))

words = clean_quote.split(" ")
print(words)
print("Number of words = " + str(len(words)))

# how many unique word 
words_set = set(words)
print("Number of unique words = " + str(len(words_set)))