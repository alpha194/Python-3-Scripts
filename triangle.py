def print_iso_triangle(n):
    ''' Function that prints out a iso triangle from the given n'''
    for value in range(0, n):
        space = " "
        num_spaces_1 = n - value - 1
        num_spaces_2 = 2 * value + 1
        print(num_spaces_1 * space + num_spaces_2 * '*')


print_iso_triangle(3)
