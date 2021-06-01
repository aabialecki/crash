import Game, account


user = {} #User Object Placeholder
inp = "" #Input Placeholder for While loop

#MENUS
login_menu = {
    "message": "Login(L) or Register(R) or Quit(Q): ",
    "options": ["L","R","Q"],
    "L": account.login,
    "R": account.register,
    "Q": quit}

main_menu = {
    "message": "Play Game(P) or View Stats(S) or Logout(L): ",
    "options": ["P","L","V"],
    "P": Game.play,
    "L": account.User.logout,
    "V": account.User.stats} #there will be an error here because it does not know which user object is being referred to


#Checks if the user input matches one of the params in valid_inputs
#if it does not, it will continue asking the user to correct their input
def check_input(menu):
    isValid = False
    user_input = input(menu["message"]).upper()
    while not isValid:
        for i in menu["options"]:
            if i == user_input:
                isValid = True
        if not isValid:
            print("Invalid Input!")
            user_input = input(menu["message"]).upper()
    return user_input


#Calls functions from a dictionary depending on user input. 
#Returns a user object containing the info of the user
#the () at the end is to convert the function referance to a function call
while inp != "Q":
    inp = check_input(login_menu)
    user = login_menu[inp]()
    while inp != "LOGOUT" and inp != "Q":
        inp = check_input(main_menu)
        main_menu[inp](user)
        if inp == "L": inp = "LOGOUT"

def quit():
    print("Quitting.")
    