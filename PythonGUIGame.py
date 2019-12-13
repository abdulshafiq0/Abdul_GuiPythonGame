from guizero import *
from random import *


name ="";

LogIn = App(title="Log In", layout="grid",width=400, height=415)
LBUsernames = ListBox(LogIn,grid=[0,1],width = 30,height = 20)
cya = Text(LogIn,text = "Choose Your \n Account:",grid = [0,0])
TXTPassword= Text(LogIn,text="Password:",grid=[1,0])
TBPassword =TextBox(LogIn,grid=[1,1],width = 25)



NewUserF = App(title="NewUser", width=300, height=175, layout="grid")
NewUserF.hide()
newusertext = Text(NewUserF,text="Username:",grid=[0,1])
newpasstext = Text(NewUserF,text="Password:",grid=[0,2])
newsecoundpasstext = Text(NewUserF,text="Confirm Password:",grid=[0,3])
TBnewusername =TextBox(NewUserF,width=25,grid=[1,1])
TBnewpassword =TextBox(NewUserF,width=25,grid=[1,2])
TBnewcpassowrd =TextBox(NewUserF,width=25,grid=[1,3])

GameF = App(title=name, width=300, height=175, layout="grid")
Score = Text(GameF,text="Score = 0",grid=[3,0])
GameF.hide()

Msgbox = App(title = "Message",height = 75)
msg = Text(Msgbox,text = "",grid = [0,0])
Msgbox.hide()

def MsgBoxClose():
    Msgbox.hide()

def MessageBox(message):
    msg.value = message
    Msgbox.show()
def GetUsernames():
    f = open("Users.txt","r")
    for line in f:
         arr = line.split("/")
         LBUsernames.append(arr[0])
    f.close()

def CheckUser():
    with open("Users.txt",mode="r") as f:
        for line in f:
            if(line == LBUsernames.value+"/"+TBPassword.value):
                GameF.show();
                GameF.title = LBUsernames.value
                LogIn.hide()
                return
    MessageBox("Invalid Username or Password")

def MakeNewUser():
    if(TBnewusername.value!=""and TBnewpassword.value !="" and TBnewcpassowrd.value!=""):
        if(TBnewpassword.value==TBnewcpassowrd.value):
            with open("Users.txt",mode="r") as f:
                for line in f:
                    arr = line.split("/")
                    if(arr[0]==TBnewusername.value):
                        MessageBox("User already exists , please choose another one")
                        return
            with open("Users.txt",mode="a+") as f:
                f.writelines("\n"+TBnewusername.value+"/"+TBnewpassword.value)
            NewUserF.hide()
            LogIn.show()
            MessageBox("Account Created")
            TBnewusername.value=""
            TBnewcpassowrd.value = ""
            TBnewpassword.value = ""
            LBUsernames.clear()
            GetUsernames()
        else:
            MessageBox("Passwords dont match")
    else:
        MessageBox("Please dont leave values empty")
def NewUser():
    LogIn.hide()
    NewUserF.show()
def BackToLogIN():
    LogIn.show();
    NewUserF.hide()
    TBnewusername.value=""
    TBnewcpassowrd.value = ""
    TBnewpassword.value = ""
def ChooseRock():
    Play(0)
def ChoosePaper():
    Play(1)
def ChooseScissors():
    Play(2)

def Play(PlayerChoice):
    choice = randint(0,2)
    print(choice)
    strp = Choice(PlayerChoice)
    strc = Choice(choice)
    if(choice == PlayerChoice):
        MessageBox("You chose "+strp+" Computer chose "+strc+" \n So draw")
    elif(choice ==0 and PlayerChoice==1):
        MessageBox("You chose "+strp+" Computer chose "+strc+" \n So you win")
    elif(choice == 0 and PlayerChoice == 2):
        MessageBox("You chose "+strp+" Computer chose "+strc+" \n So your lose")
    elif(choice ==1 and PlayerChoice == 0):
        MessageBox("You chose "+strp+" Computer chose "+strc+" \n So you lose")
    elif(choice ==1 and PlayerChoice == 2):
        MessageBox("You chose "+strp+" Computer chose "+strc+" \n So you win")
    elif(choice == 2 and PlayerChoice == 0):
        MessageBox("You chose "+strp+" Computer chose "+strc+" \n So you win")
    elif(choice ==2 and PlayerChoice ==1):
        MessageBox("You chose "+strp+" Computer chose "+strc+" \n So you lose")

def Choice(num):
    if num == 0:
        return "Rock"
    elif num  ==1:
        return "Paper"
    elif num ==2:
        return "Scissors"

BTNClose = PushButton(Msgbox,command = MsgBoxClose,text="Ok",grid=[0,1])
BTNConfirm = PushButton(LogIn,command = CheckUser,text="Confirm",grid=[1,4])
BTNNewUser = PushButton(LogIn,command = NewUser,text="New User?",grid = [0,4])
BTNnuConfirm = PushButton(NewUserF,command = MakeNewUser,text="Confirm",grid=[1,4])
BTNBack = PushButton(NewUserF,command = BackToLogIN,text="Back To \n Log In",grid=[0,5])
BTNRock = PushButton(GameF,command = ChooseRock ,text="Rock",grid=[0,0])
BTNPaper = PushButton(GameF,command = ChoosePaper,text="Paper",grid=[0,1])
BTNScissors = PushButton(GameF,command = ChooseScissors,text="Scissors",grid=[0,2])


GetUsernames()

GameF.display()

LogIn.display()

