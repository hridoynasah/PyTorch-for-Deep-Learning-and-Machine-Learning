# Default parameters
x = 10
y = 20

def my_sum(my_x = x, my_y = y, emni=None):  # Explicit parameters
    print(my_x + my_y)
    if emni is not None:
        print(emni)

my_sum(emni=10)