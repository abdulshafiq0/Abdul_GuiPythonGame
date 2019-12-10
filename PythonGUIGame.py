from guizero import *



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

BTNClose = PushButton(Msgbox,command = MsgBoxClose,text="Ok",grid=[0,1])
BTNConfirm = PushButton(LogIn,command = CheckUser,text="Confirm",grid=[1,4])
BTNNewUser = PushButton(LogIn,command = NewUser,text="New User?",grid = [0,4])
BTNnuConfirm = PushButton(NewUserF,command = MakeNewUser,text="Confirm",grid=[1,4])
BTNBack = PushButton(NewUserF,command = BackToLogIN,text="Back To \n Log In",grid=[0,5])

GetUsernames()

GameF.display()

LogIn.display()

