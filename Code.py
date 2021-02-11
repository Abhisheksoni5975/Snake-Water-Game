import random 
a=random.randint(1,3)
if(a==1):
    com='s'
elif(a==2):
    com='w'
elif(a==3):
    com='g'
user=input("Choose Snake(s) || Water(w) || Gun(g): ")
a=['s','g','w']    

print(f"Computer Choses {com}")
def GameWin(com,user):
    if(com==user):
        result=None
    elif(com=='g'):
        if(user=='s'):
            return False
        elif(user=='w'):
            return True
    elif(com=='w'):
        if(user=='s'):
            return True
        elif(user=='g'):
            return False
    elif(com=='s'):
        if(user=='g'):
            return True
        elif(user=='w'):
             return False

if user in a:
    result=GameWin(com,user)
    if(result==None):
        print("Match is Tie")
    elif(result):
         print("You are the winner")
    else:
        print("You lost")
else:
    print("Warning: Choose Correct Value from s for snake ||  w for water || g for gun")

    
