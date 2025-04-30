from collections import Counter


class InvalidInputError(Exception):

    def __init__(self, message="Введені символи повинні бути літерами"):
        self.message = message
        super().__init__(self.message)

def word_generator(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.strip().split():
                cleaned = ''.join(c.lower() for c in word if c.isalpha())
                if cleaned:
                    yield cleaned

def find_valid_words(chars, filename="KostenkoLina.txt"):
    if not all(c.isalpha() for c in chars):
        raise InvalidInputError()

    chars = chars.lower()
    chars_counter = Counter(chars)

    found_words = set()

    for word in word_generator(filename):
        if can_build_word(word, chars_counter):
            found_words.add(word)

    return found_words

def can_build_word(word, available_chars_counter):
    word_counter = Counter(word)
    return all(word_counter[c] <= available_chars_counter.get(c, 0) for c in word_counter)

def split_poems(text):
    lines = text.strip().split('\n')
    poems = []
    current_poem = []

    for line in lines:
        stripped = line.strip()
        current_poem.append(stripped)

        if stripped == "Ліна Костенко":
            poems.append('\n'.join(current_poem).strip())
            current_poem = []

    return poems
poems = split_poems(text)

for _ in range(len(poems)):
    


if __name__ == "__main__":
    try:
        user_input = input("Введіть літери: ")
        result = find_valid_words(user_input)
        if result:
            print("Знайдені слова:", ", ".join(sorted(result)))
        else:
            print("Жодне слово не знайдено.")
    except InvalidInputError as e:
        print(f"Помилка: {e}")
