#
#Python:    3.10
#
#Author:    Stephen Brinkman
#
#Purpose:   Simple text game to practive coding in Python
#

def start():
    print("Hello {}!".format(get_name()))

def get_name():
    name = input("What is your name? ")
    return name





if __name__ == "__main__":
    start()
