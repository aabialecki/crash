import database
def get_login_details():
    username = input("Enter a username (alphanumerical 1-10 chars): ")
    password = input("Enter a password (alphanumerical 1-10 chars): ")
    return {"username": username,
            "password": password}

def login():
    #Get Details
    login_details = get_login_details()
    username = login_details.get("username")
    #Check if account exists
    while not database.find_user(username):
        print("Either your login info is invalid or the user does not exist, try again!")
        login_details = get_login_details()
    #Load balance
    username = login_details.get("username")
    balance = database.get_balance(username)
    login_details["balance"] = balance
    return User(login_details)

def register():
    #Get Details
    user_details = get_login_details()
    username = user_details.get("username")
    #Check if account exists
    while database.find_user(username):
        print("Username Already Exists, Pick Another")
        user_details = get_login_details()
        username = user_details.get("username")
    #Add account to database
    user_details["balance"] = 1000
    database.new_user(user_details)
    return User(user_details)

class User(): 
    balance = 0
    username = ""
    password = ""
    def __init__(self, user_details):
        self.username = user_details.get("username")
        self.password = user_details.get("password")
        self.balance = user_details.get("balance")
        print("Bal: ", self.balance)

    def update_balance(self, amount):
        self.balance+=amount

    def logout(self):
        database.set_balance(self.username, self.balance)

    def stats(self):
        print("Stats:")

    def get_balance(self):
        return self.balance;
