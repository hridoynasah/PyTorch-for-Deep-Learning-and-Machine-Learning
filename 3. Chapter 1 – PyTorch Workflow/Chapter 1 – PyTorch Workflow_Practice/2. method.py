# Default parameters
# x = 10
# y = 20

def my_sum(my_x = 10, my_y = 20, emni=None):  # Explicit parameters
    print(my_x + my_y)
    if emni is not None:
        print(emni)

my_sum(emni=30)