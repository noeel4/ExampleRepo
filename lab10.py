# ----------------------------------------------------
#       Names: <Noel CHavez >
#    Filename: playlist.py
#        Date: <TODAY'S DATE HERE>
#
# Description: This file contains a working version
#              of Lab 8: YouTube playlist.
#
#              Your goal is to re-write this code 
#              using OBJECT-ORIENTED PROGRAMMING.
# ----------------------------------------------------
import random 

class Pokemon:
    
###~~~~~~~~~~~~~~~~~~~~~~WE GOOGLED THIS~~~~~~~~~~~~~~~~~~~###
### SOURCE: Charles Marsh, BCS Princeton University        ###
### URL: https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide ###
### INFO TAKEN: Class vs instance attributes; specifically,
###             we didn't know how to set a global attribute.
###             We mistakenly prefixed our variables with 'self.'
    
    pokemon_type="NORMAL"

###~~~~~~~~~~END OF GOOGLED CONTENT~~~~~~~~~~~~~~~~~~~~~~~~###
    
    def __init__(self,name):
        
        self.name=name
        self.max_hp=random.randint(0,100)
        self.current_hp=self.max_hp
        self.attack_power=random.randint(0,30)
        self.defensive_power=random.randint(0,50)
        self.fainted=False
        self.revives=1
        
    def printStats(self):
        print(self.name.upper(),"Type:",self.pokemon_type)
        print("HP:",self.current_hp,"/",self.max_hp)
        print("Attack:",self.attack_power)
        print("Defense:",self.defensive_power)
        

    def defend(self):
        if self.current_hp > 0:
            self.current_hp -=(self.defensive_power)
            if self.current_hp < 0:
                self.current_hp=0
                
        else:
            self.fainted=True

    def attack(self,opponent):
        opponent.defend()

    def revive(self):
        if self.fainted and (self.revives > 0 ):
            self.current_hp=self.max_hp/2
            self.revives-=1
            self.fainted=False
            return True
        else:
            return False

class Squirtle(Pokemon):

    pokemon_type="WATER"

    def selfAttack(opponent):
        if(opponent.type == "FIRE"):
            print("super effective!")
            self.attack*2
        elif(opponent.type == "GRASS" or opponent.type == "DRAGON"):
            print("not-effective")
            self.attack/2

class Charizard(Pokemon):

    pokemon_type="FIRE"

    def selfAttack(opponent):
        if(opponent.type == "GRASS"):
            print("super-effective")
            self.attack * 2

        elif (opponent.type == "WATER" or opponent.type == "FLYING"):
            print("not-effective")
            self.attack/2

class Ivysaur(Pokemon):

    pokemon_type="GRASS"

    def selfAttack(opponent):
        if(opponent.type == "WATER"):
            print("super-effective")
            self.attack * 2

        elif(opponent.type == "FIRE" or opponent.type == "STEEL"):
            print("non-effective")
            self.attack / 2
            
    
            
            
        
    
    
           
def battle(p1,p2):
   p1.printStats()
   print()
   p2.printStats()
   while not p1.fainted and not p2.fainted:
       print()
       print("p1 attacking p2")
       p2.attack(p1)
       p2.printStats()
       print()
       p1.attack(p2)       #p1 attacks p2 
       p1.printStats()
       print()
       if p2.fainted:
           print("p2 has fainted")
           if p2.revive():
               print("p2 was revived!")
               p2.attack(p1)
               print()
               p1.printStats()
               print("p2 starts attacking p1")
               if p1.fainted:
                   print("p1 fainted")
                   if p1.revive():
                       p1.printStats()
                       print("p1 was revived!")
                   else:
                        print("p1 was Unable to revive!")
           else:
                print("Unable to revive p2")
#Print the message to the winner 
   if p2.fainted:
        print(p1.name, "Wins!")
   else:
        print(p2.name,"Wins!")

    
        
            
        
                           
            
            
            
    
            
            

def main():
    p1=Pokemon("Noel")
    p2=Pokemon("Jordan")
    battle(p1,p2)
            
        
        

main()


            
            
            
        
        


        
        

        
        
    
