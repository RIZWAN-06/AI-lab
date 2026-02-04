example = [1,2,3,4,5,6,7]
from random import shuffle
shuffle(example)

print (example)

#now let's create our own shuffle function  
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

print(shuffle_list(example))


#we gonna create a few functions to attempt to mimic the carnival gussing gamr "Three Cup Monte"
my_list=[" ","0",""]
#we gonna use (" ", "0", " ") this 0 is our ball 
#eventually we gonna calling shuffle_list to shuffle the "0"
print(shuffle_list(my_list))

#next we gonna create a function that can take user input to guess wheather the "0" is on the same spot or not tht user choosed
def player_guess():
    #we gonna use a placeholder
    guess = ""
    while guess not in ['0', '1', '2']:
        guess = input ("pick a number 0, 1, 2 ")
    return int(guess)
print(player_guess())

#Now we ned one more function to actually combine all the function, whicj is essential, that list that has been shuffle with the player guess.
#remember to input the argument in vorrect order 1st list then guess
def check_guess(my_list, player_guess):
    if my_list[guess] == "0":
        print("Correct!")
    else:
        print("Incorrect!")
        print(my_list)

#Now let's setup the logic as a final script

#Initial_list
my_list = [" ", "0", " "]

#shuffle_list
mixedup = shuffle_list(my_list)

#player_guess
guess = player_guess()

#check_guess
(check_guess(mixedup, guess))
