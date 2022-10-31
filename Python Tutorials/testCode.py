

mySentance = 'loves the color'

color_list = ['red','blue','pink','teal','black']


#function
def color_function(name):
    lst = []
    for i in color_list:
        msg = '{0} {1} {2}'.format(name,mySentance,i)
        lst.append(msg)
    return lst

def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print("you need to provide your name!")
        elif name == "Stephen":
            print("Stephen you may not use this software!")
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)

get_name()

