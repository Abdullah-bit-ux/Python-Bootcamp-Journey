import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_choices=[rock,paper,scissors]
user_choice=int(input("Type 0 for rock,1 for paper,2 for scissors:"))
if user_choice>=3 or user_choice<0:
    print("Invalid Number")
else:
    print(game_choices[user_choice])
    bot_choice=random.randint(0,2)
    print(game_choices[bot_choice])

    if user_choice==bot_choice:
        print("It's a tie")
    elif user_choice==0 and bot_choice==2:
        print("You won")
    elif user_choice==1 and bot_choice==0:
        print("You won")
    elif user_choice==2 and bot_choice==1:
        print("You won")
    else:
        print("Computer Won")


