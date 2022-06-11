


from random import random
import re
import random
import string


def play_game(playerOpt):
    mylist = ["s", "r", "p"]
    
    computer =random.choice(mylist)
    
    
    if(playerOpt == computer):
          print('player enter ', playerOpt, '  ', 'computer played', computer)
          print("the computer and player pick the same move")
          return 0
    elif(playerOpt=='s'):
          if(computer=='r'):
             print('player enter ', playerOpt, '  ', 'computer played', computer)
             print("Computer won")
             return 1  
    elif(playerOpt=='r'): 
          if(computer=='p'):
             print('player enter ', playerOpt, '  ', 'computer played', computer)
             print("Computer won") 
             return 1
    elif(playerOpt=='p'):
           if(computer=='s'):
             print('player enter ', playerOpt, '  ', 'computer played', computer)
             print("Computer won")
             return 1
    
    elif(playerOpt=='r'):
          if(computer=='s'):
              print('player enter ', playerOpt, '  ', 'computer played', computer)
              print("player won") 
              return 1
    
    elif(playerOpt=='p'):
          if(computer=='r'):
             print('player enter ', playerOpt, '  ', 'computer played', computer)
             print("player won")   
             return 1  
    elif(playerOpt=='s'):
          if(computer=='p'):
             print('player enter ', playerOpt, '  ', 'computer played', computer)
             print("Player won")
             return 1
       
    else:
      print('The value entered is invalid try again')
      return 0
           
          
    
    
          
          
        
      

    


played_game =(play_game(input("Play game by enter either s, r or p")))

while(played_game==0):
     played_game =(play_game(input("Play game by enter either s, r or p")))
      
else:
      
      print('Game Ends')
      
