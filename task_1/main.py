import re


def load_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        # first line is text
        text = file.readline().strip()
        # second line is word bank
        word_bank = file.readline().strip().split(" ")
    return text, word_bank


def cut_words(text):
    """
    cut text into words and non-words (delimiters + non-words before and after every word)
    search for words and save them, everything before and after those gets saved to non_words
    """
    # add first empty string, so that after every word there comes a non_word -> easier to loop through
    words = [""]
    non_words = []
    # gets shorter with every search
    current_text = text
    # find underlines or word chars
    match = re.search(r"(_|\w)+", current_text)
    # when there isn't a single word in the text
    if match is None:
        raise ValueError("No word found!")
    while match:
        # beginning index of word
        start = match.span(0)[0]
        # index directly after end of word
        end = match.span(0)[1]

        # non_word is part before word
        non_words.append(current_text[0:start])
        # word itself
        words.append(current_text[start:end])

        # remove just saved separator and word from current_text
        current_text = current_text[end:]
        # search for another word
        match = re.search(r"(_|\w)+", current_text)
    # save chars after last word as separator
    non_words.append(current_text)
    return words, non_words


def does_match(word, possible_replacement):
    """
    is possible_replacement able to replace incomplete_word?
    """
    # does the length match?
    if len(word) != len(possible_replacement):
        return False
    # check every character
    for char_word, char_replacement in zip(word, possible_replacement):
        # when the current char in the replacement word is not unknown (isn't "_"),
        # it has to match with the current char of the word otherwise there is no chance of replaceability
        if char_word != "_" and char_word.upper() != char_replacement.upper():
            return False
    return True


def find_replacements(word, word_bank):
    """
    find every word from the word bank that could replace the word
    """
    # indices of possible replacements
    replacement_indices = []
    # search through every word from the word bank
    for word_idx, possible_replacement in enumerate(word_bank):
        # when the current word can be used as a replacement
        if does_match(word, possible_replacement):
            # save replacement index
            replacement_indices.append(word_idx)
    return replacement_indices


def replace_incomplete_words(words, word_bank):
    """
    recursive function
    take incomplete words and a word bank and replace every word with a suitable replacement from the word bank
    """

    # there are no words left to be replaced -> break recursion
    if len(words) == 0:
        return []

    # no blanks in the current word -> word is already complete
    if "_" not in words[0]:
        # save the word itself, not a replacement and run this function without the first word and the same word bank
        result = [words[0]] + replace_incomplete_words(words[1:], word_bank)
        # when the result is None, no solution can be found
        hit = result is not None
    else:
        # find replacements for the first word
        replacement_indices = find_replacements(words[0], word_bank)

        # result words
        result = []
        # True when at least one of the replacements doesn't produce any problems with the following words
        hit = False
        for replacement_idx in replacement_indices:
            # copy word bank so that the original list doesn't get altered
            current_word_bank = word_bank.copy()
            # save found replacement and remove it from the current bank
            replacement = current_word_bank.pop(replacement_idx)
            # execute this function without the first word and without the used replacement from the bank
            following_replacements = replace_incomplete_words(words[1:], current_word_bank)
            # when a solution (for every following word) with the used replacement can be found, break and return result
            if following_replacements is not None:
                result = [replacement] + following_replacements
                hit = True
                break
    if hit:
        return result
    else:
        # no solution can be found, even if there might be a suitable replacement for the first word
        return None


def main():
    text, word_bank = load_file("beispieldaten/raetsel4.txt")
    words, non_words = cut_words(text)
    words = replace_incomplete_words(words, word_bank)

    # print result, one word always comes before a separator
    for word, separator in zip(words, non_words):
        print(word, separator, sep="", end="")


if __name__ == "__main__":
    main()
