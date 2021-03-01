#practice for github
import random
import time

#greet client and get name
name = input("What's your name?: ")
time.sleep(0.5)
print("Hello", name)
time.sleep(0.5)

#function that randomizes 9 possible 8ball ans
def eightBall_answer():
  random_number = random.randint(1, 9)
  if random_number == 1:
    answer = "Yes - definitely."
  elif random_number == 2:
    answer = "It is decidedly so"
  elif random_number == 3:
    answer = "Without a doubt."
  elif random_number == 4:
    answer = "Reply hazy, try again."
  elif random_number == 5:
    answer = "Ask again later."
  elif random_number == 6:
    answer = "Better not tell you now."
  elif random_number == 7:
    answer = "My sources say no."
  elif random_number == 8:
    answer = "Outlook not so good."
  elif random_number == 9:
    answer = "Looks like BUTTCHEEKS for you!"
  return answer

#function that generates the 8balls response to client
def response(m8ball_ans):
  print("Well {}... here's my answer to you:".format(name))
  time.sleep(0.5)
  print(m8ball_ans)


#function to get the correct user input to start the game
def user_wants_to_play():
    check = str(input("Would you like to know what will hapapen in the future? (Y/N): ")).lower().strip()
    try:
        if check[0] == 'y':
            return True
        elif check[0] == 'n':
            return False
        else:
            print("Please answer 'Yes' or 'No' ")
            return user_wants_to_play()
    except Exception as error:
        print("You have to type something!")
        time.sleep(0.5)
        print("Ssssssoooooooooooo!!!!!")
        return user_wants_to_play()


user_playing = user_wants_to_play()

while user_playing == True:
  m_ball_says = eightBall_answer()
  client_question = input("What do you want to know? ")
  response(m_ball_says)
  user_playing = user_wants_to_play()

