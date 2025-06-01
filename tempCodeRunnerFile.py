import random
import hangman_stages
import word_list
import Main_Menu
Main_Menu.menu()
#\word_list=["apple","beautiful","potato"]
lives=5
chosen_word=random.choice(word_list.words)
#print(chosen_word)
display=[] # Print blank
for i in range(len(chosen_word)):
    if(i==0):
        display+=chosen_word[i]
    elif(i== (len(chosen_word)-1)):
        display+=chosen_word[i]
    else:
        display += '_'
print(display)
game_over=False
while(not game_over):
    guessed_letter = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if (letter == guessed_letter):
            display[position] = guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives==0:
            game_over=True
            print("You Lose!!")
    if '_' not in display:
        game_over=True
        print("You Win!!")
    print(hangman_stages.stages[lives])