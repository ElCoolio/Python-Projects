#
#Python:    3.10
#
#Author:    Stephen Brinkman
#
#Purpose:   Simple text game to practive coding in Python
#


def start(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)



def describe_game(name):
    """
        Check if this is a new game or not.
        if it is new, get the user's name.
        if it is not a new game, thank the user
        for playing again and continue with the game
    """
    #meaning, if we do not already have this user's name,
    # then they are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be  sealed by your actions.")
                    stop = False
    return name



def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>:").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print ("\nThe stranger glares at you \nmenancingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()



def show_score(nice,mean,name):
    if nice > mean:
        print ("\nThe sun is shining!")
    if nice < mean:
        print ("\nClouds blot out the sun!")
    if nice == mean:
        print ("\nAnything could happen")



def score(nice, mean, name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: # if the condition is valid, call win function passsing in variables so it can use them
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:        # else call nice_mean function in the carible so it can use them
        nice_mean(nice,mean,name)



def win(nice,mean,name):
    #substitiute the {} wild cards with our vaiable values
    playsound(winGame.mp3)
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    # call again funciton and pass in our variables
    again(nice,mean,name)



def lose(nice,mean,name):
    #substitiute the {} wild cards with our vaiable values
    playsound(loseGame.mp3)
    print("\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan down by the river, wretched and alone!".format(name))
    # call again funciton and pass in our variables
    again(nice,mean,name)
    



def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', and ( N ) for 'NO':\n>>> ")



def reset(nice,mean,name):
    nice = 0;
    mean = 0;
    # Notice, I do not reset the name variable as the same user has elected to play again
    start(nice,mean,name)

if __name__ == "__main__":
    start()
