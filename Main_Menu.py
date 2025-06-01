import hangman_stages
def menu():
    print("Welcome to Hangman Game")
    s="Press any Key to continue"
    print(s.center(20,'*'))
    n = input()
    clear_screen()
def clear_screen():
    print("\n"*50)
    print("\n"*50)