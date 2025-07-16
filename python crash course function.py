# create a function
def print_x_time(parameter, loop_amount = 5):
    counter = 0
    while counter < loop_amount:
        print(counter, parameter)
        counter += 1

# call the function
print("print")
print_x_time("test")