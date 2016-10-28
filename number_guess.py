def guess_game():
  import random
  answer = random.randint(1, 2)
  print answer
  ask_user = raw_input('Guess a number between 1 and 50: ')
  
  def ask_again(correctNumber):
    answer = correctNumber
    ask_user_again = raw_input('Try again: ')
    if ask_user_again == answer:
      print "Correct! the answer was: %d." % answer
    elif ask_user_again > answer:
      print "Incorrect. Pick a smaller number."
      ask_again(answer)
    else:
      print "Incorrect. Pick a larger number."
      ask_again(answer)

  if ask_user == answer:
    print "Correct! the answer was: %d." % answer
  elif ask_user > answer:
    print "Incorrect. Pick a smaller number."
    ask_again(answer)
  else:
    print "Incorrect. Pick a larger number."
    ask_again(answer)

guess_game()