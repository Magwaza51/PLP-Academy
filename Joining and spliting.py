cats = "Annie,Neo,Salem,Sabrina,Marv,Agatha"

# Split list
cat_list = cats.split(",")
print(cat_list)

# Join list back
rejoined_lint = " | ".join(cat_list[-1:: -1])
print(rejoined_lint)