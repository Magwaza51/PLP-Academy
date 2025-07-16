# A funtion to square a number
def get_square(n):

    # work out the square
    this_square = n ** n
    return this_square

# Where to start and stop
start_number = 1
stop_number = 10

# Print out first N squares
for integer in range(1 , stop_number + 1):


    # Call a separate funtion to square this number
    int_squared = get_square(integer)

    # Print out this square
    print("Squara of {0:3} is {1:3}".format(integer,int_squared))