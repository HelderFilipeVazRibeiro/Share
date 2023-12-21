
def main():
    print_column(4)

def print_column(height):
    print("#\n" * height, end="")
    
main()
"""
def main():
    print_row(4)

def print_row(width):
    print("#" * width, end=" \n")
    
main()
"""
"""
def main():
    print_square(5)

def print_square(size):
    #for each row in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            #print brick
            print("#", end="")
        print()

main()

"""