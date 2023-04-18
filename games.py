import random

money = 100

import random
money = 100

#Coin Toss
def flip_coin(guess, bet):
  global money
  if bet > money:
    print("Sorry, you don't have that much money! Try a lower bet.")
    print()
    return 0
  elif bet < 0:
    print("You can't bet a negative! Try a positive bet value.")
    print()
    return 0
  else:
    print("Let's flip a coin!")
  guessed = guess.lower()
  if guessed != 'heads' and guess != 'tails':
    print("Please guess either 'heads' or 'tails'.")
    print()
    return 0
  num = random.randint(1,2)
  print("Coin is flipping...")
  if num == 1:
    print("It's heads!")
  elif num == 2:
    print("It's tails!")  
  if guessed == "heads" and num == 1:
    print("You win! You won " + str(bet) + ".")
    print()
    return bet
  elif guessed == "tails" and num == 2:
    print("You win! You won " + str(bet) + ".")
    print()
    return bet
  else:
    print("Sorry, try again! You lost " + str(bet) + ".")
    print()
    return bet * -1
 
money += flip_coin('heads', 8)
money += flip_coin('tails', 8)
money += flip_coin('heads!', 8)
money += flip_coin('heads', 200)
money += flip_coin('tails', -3)

#Chohan
def play_chohan(guess, bet):
  global money
  if bet > money:
    print("Sorry, you don't have that much money left! Try a lower bet.")
    print()
    return 0
  elif bet < 0:
    print("You can't bet a negative! Try a positive bet value.")
    print()
    return 0
  else:
    print("Let's play chohan!")
  guessed = guess.lower()
  if guessed != 'even' and guess != 'odd':
    print("Please guess either 'even' or 'odd'.")
    print()
    return 0
  print("Dice are rolling...")
  num1 = random.randint(1,6)
  num2 = random.randint(1,6)
  dice = num1 + num2
  if dice % 2 == 0:
    print("It's even!")
  else:
    print("It's odd!")
  if (guessed == 'even' and dice % 2 == 0) or (guessed == 'odd' and dice % 2 == 1):
    print("You win! You won " + str(bet) + ".")
    print()
    return bet
  else:
    print("Sorry, try again! You lost " + str(bet) + ".")
    print()
    return bet * -1

money += play_chohan('even', 3)
money += play_chohan('odd', 4)
money += play_chohan('evens', 3)
money += play_chohan('even', 300)
money += play_chohan('even', -3)


#Pick A Card
def pick_cards(bet):
  global money
  if bet > money:
    print("Sorry, you don't have that much money left! Try a lower bet.")
    print()
    return 0
  elif bet < 0:
    print("You can't bet a negative! Try a positive bet value.")
    print()
    return 0
  else:
    print("Let's pick cards!")
  print("Choosing cards...")
  player1 = random.randint(1,52)
  player2 = random.randint(1,52)
  if player1 > player2:
    print("Player 1 wins!")
  elif player2 > player1:
    print("Player 2 wins!")
  else:
    print("It's a tie!")
  if player1 > player2:
    print("You win! You won " + str(bet) + ".")
    print()
    return bet
  elif player2 > player1:
    print("Sorry, try again! You lost " + str(bet) + ".")
    print()
    return bet * -1
  else:
    print("Almost! Try again! No money changed hands.")
    return 0

money += pick_cards(4)
money += pick_cards(400)
money += pick_cards(-4)


#Roulette
def play_roulette(guess, bet):
  global money
  if bet > money:
    print("Sorry, you don't have that much money left! Try a lower bet.")
    print()
    return 0
  elif bet < 0:
    print("You can't bet a negative! Try a positive bet value.")
    print()
    return 0
  else:
    print("Let's play roulette!")
  if type(guess) is str:  
    guessed = guess.lower()
    if guessed != 'even' and guessed != 'odd':
      print("Please guess 'even' or 'odd' or a number on the roulette wheel.")
      print()
      return 0
  elif type(guess) is int:
    if guess == 00:
      guessed = 37
    elif guess in range(37):
      guessed = guess
    else:
      print("Please enter 00 or a number 0 to 36.")
      print()
      return 0
  else:
    print("Please enter 'even', 'odd', or a number on the roulette wheel as your guess.")
    print()
    return 0
  print("Wheel is spinning...")
  num = random.randint(0,37)
  if num in range(37):
    print("It's {}!".format(num))
  else:
    print("It's 00!")
  if guessed == 'even':
    if num == 0 or num == 37:
      print("Sorry, you lost! You lost " + str(bet) + ".")
      print()
      return bet * -1
    elif num % 2 == 0:
      print("You won! You won " + str(bet) + "!")
      print()
      return bet
    else:
      print("Sorry, you lost! You lost " + str(bet) + ".")
      print()
      return bet * -1
  elif guessed == 'odd':
    if num == 0 or num == 37:
      print("Sorry, you lost! You lost " + str(bet) + ".")
      print()
      return bet * -1
    elif num % 2 != 0:
      print("You won! You won " + str(bet) + "!")
      print()
      return bet
    else:
      print("Sorry, you lost! You lost " + str(bet) + ".")
      print()
      return bet * -1
  else:
    if guessed == num:
      print("You won! You won " + str(bet * 35) + "!")
      print()
      return bet * 35
    else:
      print("Sorry, you lost! You lost " + str(bet * 35) + ".")
      print()
      return bet * -35

money += play_roulette('even', 6)
money += play_roulette('evens', 6)
money += play_roulette('even', -6)
money += play_roulette('even', 600)
money += play_roulette(0, 3)
money += play_roulette(21, 4)


