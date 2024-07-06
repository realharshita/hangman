import random
import os

def get_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'terminal']
    hints = {
        'python': 'A popular programming language.',
        'hangman': 'The game you are playing right now.',
        'challenge': 'A task or situation that tests someone\'s abilities.',
        'programming': 'The process of writing computer software.',
        'terminal': 'A command line interface for interacting with the computer.'
    }
    word = random.choice(words)
    return word, hints[word]

def display_word(word, guesses):
    return ' '.join([char if char in guesses else '_' for char in word])

def display_hangman(attempts):
    stages = [
        '''
           -----
           |   |
               |
               |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        '''
    ]
    return stages[6 - attempts]

def save_score(player_name, score):
    with open('scores.txt', 'a') as file:
        file.write(f'{player_name}: {score}\n')

def display_scores():
    if os.path.exists('scores.txt'):
        with open('scores.txt', 'r') as file:
            scores = file.readlines()
            print('\nHigh Scores:')
            for score in scores:
                print(score.strip())
    else:
        print('\nNo scores to display yet.')

def play_round():
    word, hint = get_word()
    guesses = []
    attempts = 6
    hints_used = 0

    while attempts > 0:
        print(display_hangman(attempts))
        print(f'Word: {display_word(word, guesses)}')
        print(f'Hints used: {hints_used}')
        print('Type "hint" for a hint (costs 1 attempt).')
        guess = input('Enter a letter: ').lower()

        if guess == 'hint':
            if hints_used < 1:
                print(f'Hint: {hint}')
                hints_used += 1
                attempts -= 1
            else:
                print('No hints remaining.')
        elif len(guess) != 1 or not guess.isalpha():
            print('Invalid input. Please enter a single letter.')
        elif guess in guesses:
            print('You already guessed that letter.')
        elif guess in word:
            guesses.append(guess)
            print('Correct guess!')
        else:
            attempts -= 1
            guesses.append(guess)
            print(f'Wrong guess! Attempts remaining: {attempts}')
        
        if set(word).issubset(set(guesses)):
            print(display_hangman(attempts))
            print(f'\nCongratulations! You guessed the word: {word}')
            return attempts * 10 - hints_used * 5
    else:
        print(display_hangman(attempts))
        print(f'\nGame Over! The word was: {word}')
        return 0

def main():
    print('Welcome to Hangman!')
    player_name = input('Enter your name: ')
    score = 0
    rounds = 3
    play_again = 'y'
    
    while play_again == 'y':
        for _ in range(rounds):
            score += play_round()
        
        print(f'\nYour total score after {rounds} rounds is: {score}')
        save_score(player_name, score)
        display_scores()
        play_again = input('Do you want to play again? (y/n): ').lower()
        if play_again == 'y':
            score = 0
            print('\nStarting a new game!')
    
    print('Thanks for playing Hangman!')

if __name__ == "__main__":
    main()
