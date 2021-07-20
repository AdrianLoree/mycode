#!/usr/bin/env python3
'''challenege to create a guessing game with multiple choice questsions By Adrian'''

#script function
def main():
    '''loads at runtime'''

#user input to answer the question
    guess= input("What is Bruce Wayne's secret identity?")

#compare the guess to the correct answer and converts all text to lower so it will always match
    if guess.lower() == "batman":
        #tell the user that they got the right answer
        print("Correct Batman is Bruce Wayne's secret identity! Congrats!")
   
   #if the answer is the expected result tell them they did not get the question correct
    else:
         print("Sorry that is not correct... :(")

#runs the script        
main()
