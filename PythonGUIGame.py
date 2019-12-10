from guizero import *



name ="";
LogIn = App(title="Log In", width=300, height=175, layout="grid")
LBUsernames = ListBox(LogIn,grid=[0,0])

#message = Text(LogIn,text = "Login:",grid = [0,0])
#utext = Text(LogIn,text="Username:",grid=[0,1])
#TBusername = TextBox(LogIn,width=25,grid=[1,1])
#ptext=Text(LogIn,text="Password:",grid=[0,2])                       
#TBpassword = TextBox(LogIn,width=25,grid=[1,2])

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
def GetUsernames():
    f = open("Users.txt","r")
    for line in f:
         arr = line.split("/")
         LBUsernames.items.add(arr[0])
         LogIn.Display()
    f.close()
        
def CheckUser():
    print("hi")
    f = open("Users.txt","r")
    for line in f:
        if(line==TBusername.value+"/"+TBpassword.value):
            name=TBusername.value
            GameF.title = name;
            print("Logged In")
            LogIn.hide()
            GameF.show()
    f.close()
def MakeNewUser():
    if(TBnewusername.value!=""and TBnewpassword.value !="" and TBnewcpassowrd.value!=""):
        if(TBnewpassword.value==TBnewcpassowrd.value):
            with open("Users.txt",mode="r") as f:
                for line in f:
                    arr = line.split("/")
                    if(arr[0]==TBnewusername.value):
                        print("User already exists , please choose another one")
                        return
            with open("Users.txt",mode="a+") as f:
                f.writelines("\n"+TBnewusername.value+"/"+TBnewpassword.value)
            NewUserF.hide()
            LogIn.show()
            print("Account Created")
            TBnewusername.value=""
            TBnewcpassowrd.value = ""
            TBnewpassword.value = ""
        else:
            print("Passwords dont match")
    else:
        print("Please dont leave values empty")
def NewUser():
    LogIn.hide()

    TBpassword.value = ""
    TBusername.value =""
    NewUserF.show()
def BackToLogIN():
    LogIn.show();
    NewUserF.hide()
    TBnewusername.value=""
    TBnewcpassowrd.value = ""
    TBnewpassword.value = ""

BTNConfirm = PushButton(LogIn,command = CheckUser,text="Confirm",grid=[1,3])
BTNNewUser = PushButton(LogIn,command = NewUser,text="New User?",grid = [0,4])
BTNnuConfirm = PushButton(NewUserF,command = MakeNewUser,text="Confirm",grid=[1,4])
BTNBack = PushButton(NewUserF,command = BackToLogIN,text="Back To \n Log In",grid=[0,5])

GameF.display()

LogIn.display()
GetUsernames()

