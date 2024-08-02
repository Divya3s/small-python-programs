import random
l=["rock","scissor","paper"]

while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game Start.....
1 Yes                                  
2 No | Exit                 
            
                ''' ))
    
    if uc==1:
        for a in range(1,6):
            userinput=int(input('''
1 Rock                                
2 Scissor                                
3 Paper                              
                    '''))
            if userinput==1:
                uchoice="rock"
            elif userinput==2:
                uchoice="scissor"
            elif userinput==2:
                uchoice="paper"  
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("Computer value",Cchoice)
                print("Uservalue",uchoice)
                print("Game Draw")     
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice== "rock" and Cchoice=="scissor") or (uchoice== "paper" and Cchoice=="rock") or (uchoice== "scissor" and Cchoice =="paper") :
                 print("Computer value",Cchoice)
                 print("Uservalue",uchoice)
                 print("You Win")     
                 ucount=ucount+1
            else:
                print("Computer value",Cchoice)
                print("Uservalue",uchoice)
                print("Game Draw")     
                ccount=ccount+1 

        if ucount==ccount:
           print("Final Game Draw...")
           print("User Score",ucount)
           print("Computer Score",ccount)
        elif ucount>ccount:
           print("Final You Win The Game...")
           print("User Score",ucount)
           print("Computer Score",ccount) 
        else:
           print("Final Computer Win The Game...")
           print("User Score",ucount)
           print("Computer Score",ccount)   

    else:
       break