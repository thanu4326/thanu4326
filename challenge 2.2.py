#2.2 implement a class called player that represents a cricket player. the player class should have a method called play() which prints " the player is playing cricket". derive two claases batman and bowler, from the player class. override the play() method in each derived class to print " the batman is batting" and " the bowler is bowling", respectively. write a program to create a objects of both the batsman and bowler classes and call the play() method for each object.
#define the player class
 
class Player:
    def play(self):
        print("The player is playing cricket")
# define the batsman class, derived from player      
class Batman(Player):
    def play(self):
        print("The batman is batting")
#define the bowler class, derived from player      
class Bowler(Player):
    def play(self):
        print("The bowler is bowling")
        
#create objects of the derived classes
batsman = Batman()
bowler = Bowler()
#call the play() method for each object
batsman.play()
bowler.play()