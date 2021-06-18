import random
LIM = 1000 #Limit for Crash Multiplier
H = 10 #Multiplier Variable (Random Int < LIM)


def start_game(cashout_multiplier):
   return isWinner(calc_multiplier(), cashout_multiplier)

def calc_multiplier():
    H = random.randint(0,(LIM-1)) #Sets H to a random int between 0 and LIM
    multiplier = 0.99*LIM/(LIM-H)
    return multiplier

def isWinner(multiplier, cashout_multiplier):
    if cashout_multiplier > multiplier:
        return {'won':False,
                'multiplier':multiplier}
    else:
        return {'won':True,
                'multiplier':multiplier}