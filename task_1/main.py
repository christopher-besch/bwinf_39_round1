import re


def does_match(incomplete_word, full_word):
    # does the length match?
    if len(incomplete_word) != len(full_word):
        return False
    # check every character
    for char_incomplete_word, char_full_word in zip(incomplete_word, full_word):
        # when the current char in the incomplete word is not unknown the char from the full word has to match
        if char_incomplete_word != "_" and char_incomplete_word.upper() != char_full_word.upper():
            # if not the words don't match
            return False
    return True


def cut_words(text):
    """
    cut words into words and non-words (i.e. separators + non-words before and after every word)
    search for words and save them, everything before and after those gets saved to separators
    """
    # so that after every word there comes a separator -> easier to loop through
    words = [""]
    separators = []
    # gets shorter with every search
    current_text = text
    # find underlines or word chars
    match = re.search(r"(_|\w)+", current_text)
    if match is None:
        raise ValueError("No word found!")
    while match:
        # beginning index of word
        start = match.span(0)[0]
        # index directly after end of word
        end = match.span(0)[1]

        # separator is part before word
        separators.append(current_text[0:start])
        # word itself
        words.append(current_text[start:end])

        # remove just saved separator and word from current_text
        current_text = current_text[end:]
        # search for another word
        match = re.search(r"(_|\w)+", current_text)
    # save chars after last word as separator
    separators.append(current_text)

    return words, separators


def load_file(filename):
    filepath = filename
    with open(filepath, "r", encoding="utf-8") as file:
        text = file.readline().strip()
        words = file.readline().strip().split(" ")

    return text, words


def find_replacements(word, word_bank):
    replacement_indices = []
    # find replacement for text_word
    for word_idx, possible_replacement in enumerate(word_bank):
        # when the current word can be used as a replacement
        if does_match(word, possible_replacement):
            # save replacement word index
            replacement_indices.append(word_idx)
    return replacement_indices


# recursive function
def replace_incomplete_words(words, word_bank):
    # there are no words left to replace -> break recursion
    if len(words) == 0:
        return []

    # the current word is already complete -> save the word itself
    if "_" not in words[0]:
        result = [words[0]] + replace_incomplete_words(words[1:], word_bank)
        hit = result is not None
    else:
        # find replacements for the first word
        replacement_indices = find_replacements(words[0], word_bank)

        # result words
        result = []
        # True when at least one of the replacements doesn't produce any problems with the other words
        hit = False
        for replacement_word_idx in replacement_indices:
            # copy words so that the original list doesn't get altered
            current_word_bank = word_bank.copy()
            # save found replacement and remove used word from the current bank
            replacement = current_word_bank.pop(replacement_word_idx)
            # execute this function without the first word and without the used word from the bank
            other_replacement_words = replace_incomplete_words(words[1:], current_word_bank)
            # when a solution with the selected replacement word from the bank can be found, break and return result
            if other_replacement_words is not None:
                result = [replacement] + other_replacement_words
                hit = True
                break
    if hit:
        return result
    else:
        return None


def main():
    text, word_bank = load_file("beispieldaten/raetsel4.txt")
    text_words, text_separator = cut_words(text)
    text_words = replace_incomplete_words(text_words, word_bank)

    # print result, one word always comes before a separator
    for word, separator in zip(text_words, text_separator):
        print(word, separator, sep="", end="")


if __name__ == "__main__":
    main()
