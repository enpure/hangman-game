import random

'''Загрузка словаря'''


def load_words(filename):
    with open(filename, encoding='utf-8') as file:
        words = file.read().splitlines()
    return [word for word in words if len(word) > 3]


def get_random_word(words):
    return random.choice(words).upper()


'''Инициализация игры'''


def start_game():
    print("Добро пожаловать в игру 'Виселица'!")
    while True:
        choice = input("Вы хотите начать новую игру (да/нет)? ").lower()
        if choice == 'да':
            play_game()
        elif choice == 'нет':
            print("Спасибо за игру!")
            break
        else:
            print("Неверный ввод. Пожалуйста, введите 'да' или 'нет'.")


'''Игровой цикл'''


def play_game():
    words = load_words('words.txt')
    secret_word = get_random_word(words)
    guessed_word = ['_'] * len(secret_word)
    guessed_letters = []
    mistakes = 0
    max_mistakes = 6

    while mistakes < max_mistakes and ''.join(guessed_word) != secret_word:
        print(f"Слово: {' '.join(guessed_word)}")
        print(f"Ошибки ({mistakes}): {', '.join(guessed_letters)}")
        guess = input("Введите букву: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, введите одну букву.")
            continue

        if guess in guessed_letters:
            print("Вы уже отгадали эту букву.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            mistakes += 1

        display_hangman(mistakes)

    if ''.join(guessed_word) == secret_word:
        print(f"Поздравляем! Вы отгадали слово: {secret_word}")
    else:
        print(f"Вы проиграли! Загаданное слово было: {secret_word}")


'''Отображение виселицы'''


def display_hangman(mistakes):
    stages = [
        """
           ------
           |    |
           |
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           O    |
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           O    |
           |    |
           |
           |
        --------
        """,
        """
           ------
           |    |
           O    |
          /|    |
           |
           |
        --------
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
           |
           |
        --------
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          /     |
           |
        --------
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
           |
        --------
        """
    ]
    print(stages[mistakes])


'''Запуск игры'''

if __name__ == "__main__":
    start_game()
