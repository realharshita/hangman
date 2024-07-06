import random

def get_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'terminal']
    return random.choice(words)

def display_word(word, guesses):
    return ''.join([char if char in guesses else '_' for char in word])

def main():
    word = get_word()
    guesses = []
    attempts = 6
    print('Welcome to Hangman!')
    print(f'You have {attempts} attempts to guess the word.')
    
    while attempts > 0:
        print(f'\nWord: {display_word(word, guesses)}')
        guess = input('Enter a letter: ').lower()
        
        if guess in guesses:
            print('You already guessed that letter.')
        elif guess in word:
            guesses.append(guess)
            print('Correct guess!')
        else:
            attempts -= 1
            guesses.append(guess)
            print(f'Wrong guess! Attempts remaining: {attempts}')
        
        if set(word).issubset(set(guesses)):
            print(f'\nCongratulations! You guessed the word: {word}')
            break
    else:
        print(f'\nGame Over! The word was: {word}')

if __name__ == "__main__":
    main()
