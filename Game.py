import random, account
LIM = 1000 #Limit for Crash Multiplier
H = 10 #Multiplier Variable (Random Int < LIM)

def play(user):
    #Get user bet amount
    cashout_multiplier, bet = place_bet(user)
    #Calculate crash multiplier
    multiplier = calc_multiplier()
    #calculate winnings
    winnings = calc_winnings(multiplier, cashout_multiplier, bet)
    user.update_balance(winnings)
    output_game_info(user, multiplier, cashout_multiplier, bet, winnings)
    #update stats

def calc_multiplier():
    H = random.randint(0,(LIM-1)) #Sets H to a random int between 0 and LIM
    print(H)
    multiplier = 0.99*LIM/(LIM-H)
    return multiplier

def calc_winnings(multiplier, cashout_multiplier, bet):
    if cashout_multiplier > multiplier:
        winnings = 0 - bet
    else:
        winnings = bet*cashout_multiplier
    return winnings

def place_bet(user):
    balance = user.get_balance()
    print(balance)
    b_inp_msg = "Enter your bet (1-" + str(balance) + "): "
    c_inp_msg = "Enter your cashout multiplier (1-" + str(LIM) + "): "

    
    while True:
        bet = input(b_inp_msg)
        if not bet.isnumeric():
            print("Not a Number, Try Again")
        elif int(bet) > balance:
            print("Insuffucent Funds, Try placing a lower bet.")
        else:
            break
    bet = int(bet)

    while True:
        cashout_multiplier = input(c_inp_msg)
        if not isnumeric(cashout_multiplier):
            print("Not a Number, Try Again")
        elif float(cashout_multiplier) > LIM:
            print("Insuffucent Funds, Try placing a lower bet.")
        else:
            break
    cashout_multiplier = float(cashout_multiplier)
    return cashout_multiplier, bet

def isnumeric(num):
    try:
        num = float(num)
    except valueError:
        return False
    return True

def output_game_info(user, multiplier, cashout_multiplier, bet, winnings):
    print("_______________________________________________")
    print("It Crashed At: ", multiplier)
    if cashout_multiplier > multiplier:
        print("YOU LOST: $", bet)
    else:
        print("YOU WON: $", winnings)
    print("Your new balance is: $",user.get_balance())