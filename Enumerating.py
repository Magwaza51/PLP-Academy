# The wise owl cats, at the time of writing
cats = "Annie,Neo,Salem,Sabrina,Marv,Agatha"

cat_list = cats.split(",")

for cat_number, cat_name in enumerate(cat_list):
    print(f"cat_number {cat_number + 1} is {cat_name}")

