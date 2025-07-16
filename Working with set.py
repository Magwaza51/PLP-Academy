# friend
friend = {"Rachel","Phoebe","Chandler","Joey","Monica","Ross"}

# shelves
shelves = {"Ronnie-Filchner","Ross","McMurdo"}

# print these out
# print(friend)
# print(shelves)

# # Prove these are sets
# print(type(friend))
# print(type(shelves))

# union (in both set)
union = friend | shelves
print(union)

# intersection 
intersection = shelves & friend
print(intersection)

# ice shelves with aren't friends
ice_shelves_not_friend = shelves - friend
print(ice_shelves_not_friend)

# elements is either set, but not both (caret)
bob = friend ^ shelves
print(bob)