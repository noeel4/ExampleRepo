# -------------------------------------------------
#        Name: Noel Chavez, Alexis Lopez 
#    Filename: lab9.py
#        Date: July 19th, 2019
#
# Description: Noel and Alexis's submission for lab 9.
#              
# -------------------------------------------------

import random

def eightballanswers():
    read_file=open("responses.txt","r")

    text=list(read_file)

    read_file.close()

    return text



def askquestion():
    question=input("Ask a question(YES or NO):")
    response= random.choice(eightballanswers()) #choose random item from the responses text file 
    print(response)                          #prints the randomly chosen response 

def main():
    askquestion()
    next_question=input("Would you like to ask another question? YES or NO: ")
    while next_question.upper() == "YES":
        askquestion()
        next_question=input("New question? (YES or NO):")
        
        
        
    

main()
    

    
    
    


    
    
