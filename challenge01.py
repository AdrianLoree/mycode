#!/usr/bin/env python3
'''challenege to create a guessing game with multiple choice questsions By Adrian'''
#script function
print('Guess that Superhero')

def main():
    '''loads at runtime'''

    ans = "y"
    
    while ans == "y":
        #prompt user for which question they want to do
        question = input('Which question like would you like to do (1-5)? ')
        
        if question == '1':

#user input to answer the question
            guess= input("What is Bruce Wayne's secret identity? ")

#compare the guess to the correct answer and converts all text to lower so it will always match
            if guess.lower() == "batman":
        #tell the user that they got the right answer
                print("Correct Batman is Bruce Wayne's secret identity! Congrats!")



   #if the answer is the expected result tell them they did not get the question correct
            else:
                print("Sorry that is not correct... :(")
                

        if question == '2':

#user input to answer the question
            guess= input("What is Dick Grayson's secret identity? ")

#compare the guess to the correct answer and converts all text to lower so it will always match
            if guess.lower() == "nightwing":
        #tell the user that they got the right answer
                print("Correct Nightwing is Dick Grayson's secret identity! Congrats!")

   #if the answer is the expected result tell them they did not get the question correct
            else:
                print("Sorry that is not correct... :(")


        if question == '3':

#user input to answer the question
            guess= input("What is Diana Prince's secret identity? ")

#compare the guess to the correct answer and converts all text to lower so it will always match
            if guess.lower() == "wonder woman":
        #tell the user that they got the right answer
                print("Correct Wonder Woman is Diana Prince's secret identity! Congrats!")

   #if the answer is the expected result tell them they did not get the question correct
            else:
                print("Sorry that is not correct... :(")


        if question == '4':

#user input to answer the question
            guess= input("What is Barry Allen's secret identity? ")

#compare the guess to the correct answer and converts all text to lower so it will always match
            if guess.lower() == "the flash":
        #tell the user that they got the right answer
                print("Correct! The Flash is Barry Allen's secret identity! Congrats!")

   #if the answer is the expected result tell them they did not get the question correct
            else:
                print("Sorry that is not correct... :(")


        if question == '5':

#user input to answer the question
            guess= input("What is Barbara Gordon's secret identity? ")

#compare the guess to the correct answer and converts all text to lower so it will always match
            if guess.lower() == "batgirl":
        #tell the user that they got the right answer
                print("Correct Batgirl is Barnara Gordon's secret identity! Congrats!")
                
   #if the answer is the expected result tell them they did not get the question correct
            else:
                print("Sorry that is not correct... :(")
                
 
#runs the script        
main()
