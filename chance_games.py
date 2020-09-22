import random

money = 100


#Write your game of chance functions here

#COIN FLIP
def coin_flip(bet, call):
  print("Coin Toss!")
  print("----------")
  print("\n")
#Put limits on inputs
  if bet > money:
    print("You don't have enough funds!")
    return False
  if bet <= 0:
    print("Your bet must be $1 or more.")
    return False
  if isinstance(bet,int) == False:
    print("Your bet must be a multiple of $1")
    return False
#Generate random number 1 or 2, simulating coin toss
  num = random.randint(1,2)
#Compare bets to outcome, calculate returns or losses
  if call == heads:
    print("You called heads!")
    print("-----------------")
    if num == 1:
      print("......It's heads! You won " + str(bet) + " dollars!")
      return bet
    else:
      print("......Sorry, it's tails. You lost " + str(abs(bet)) + " dollars.")
      return -bet
  elif call == tails:
    print("You called tails!")
    print("-----------------")
    if num == 2:
      print("......It's tails! You won " + str(bet) + " dollars!")
      return bet
    else:
      print("......Sorry, it's heads. You lost " + str(abs(bet)) + " dollars.")
      return -bet
  


#CHO HAN
def cho_han(bet, call):
  print("Cho Han!")
  print("--------")
  print("\n")
#Put limits on inputs
  if bet > money:
    print("You don't have enough funds!")
    return False
  if bet <= 0:
    print("Your bet must be $1 or more.")
    return False
  if isinstance(bet,int) == False:
    print("Your bet must be a multiple of $1")
    return False
#Generate two random numbers from 1 to 6, simulating dice
  num1 = random.randint(1,6)
  num2 = random.randint(1,6)  
#Check parity of sums, compare to bet, and calculate returns or losses
  if call == odd:
    print("You called odd!")
    print("---------------")
    if (num1 + num2) % 2 > 0:
      print("......It's odd! You won " + str(bet) + " dollars!")
      return bet
    else:
      print("......Sorry, it's even. You lost " + str(abs(bet)) + " dollars.")
      return -bet
  if call == even:
    print("You called even!")
    print("----------------")
    if (num1 + num2) % 2 == 0:
      print("......It's even! You won " + str(bet) + " dollars!")
      return bet
    else:
      print("......Sorry, it's odd. You lost " + str(abs(bet) + " dollars."))
      return -bet


#CARD DRAW
def card(bet):
  print("Card Draw!")
  print("----------")
  print("\n")
#Put limits on inputs
  if bet > money:
    print("You don't have enough funds!")
    return False
  if bet <= 0:
    print("Your bet must be $1 or more.")
    return False
  if isinstance(bet,int) == False:
    print("Your bet must be a multiple of $1")
    return False 
#Generate card deck
#Four sets of numbers, 1 to 13 representing Ace through King
  deck = list(range(1,14))*4
#Sample the deck twice without replacement
  play = random.sample(deck, k=2)
  print("Your card is " + str(play[0]))
  print("Player two's card is " + str(play[1]))
#Check for ties or higher card, calculate returns or losses
  if play[0] == play[1]:
    print("It's a tie! All bets returned")
    return 0
  if play[0] > play[1]:
    print("Nice! Looks like you won $" + str(bet) + " dollars.")
    return bet
  else:
    print("Maybe you'll have better luck next time. You lose $" + str(abs(bet)) + " dollars.")
    return -bet


#ROULETTE
def roulette(bet, call):
  print("Roulette!")
  print("---------")
  print("\n")
#Put limits on inputs
  if bet > money:
    print("You don't have enough funds!")
    return False
  if bet <= 0:
    print("Your bet must be $1 or more.")
    return False
  if isinstance(bet,int) == False:
    print("Your bet must be a multiple of $1")
    return False
#Generate random integer from 1 to 38
  roll = random.randint(1,38)
# 0 slot is represented by i=37 and 00 by i=38
  if roll == 37:
    num = "0"
  elif roll == 38:
    num = "00"
  else:
    num = roll
  print("And the winning number is....")
  print(str(num) + "!")
#Check bets and return wins and losses
#House bets
  if roll == 37 or roll == 38:
    print("House wins! You lose all bets.")
    return -bet
#Parity
  elif call == even and roll % 2 == 0:
    print("You guessed even! You win " + str(bet) + " dollars.")
    return bet
  elif call == odd and roll % 2 != 0:
    print("You guessed odd! You win " + str(bet) + " dollars.")
    return bet
#Single
  elif call == roll:
    print("You guessed " + str(call).lower() + ". You win " + str(bet*35) + " dollars!")
    return bet*35
  else:
    print("You guessed " + str(call).lower() + ". You lost all bets.")
    return -bet

#Call your game of chance functions here
heads = "Heads"
tails = "Tails"
odd = "Odd"
even = "Even"


money += coin_flip(2.5, heads)
print("Funds: $" + str(money))
print("\n")
money += cho_han(20, odd)
print("Funds: $" + str(money))
print("\n")
money += card(20)
print("Funds: $" + str(money))
print("\n")
money += roulette(10, 4)
print("Funds: $" + str(money))
money += roulette(10, "Even")
