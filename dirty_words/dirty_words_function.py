def replace_dirty_words(text, bad_words):
    """ Service that replaces all the dirty words people use when writing comments with '*'

    :param text: input comment by user
    :param bad_words: array of words that are forbidden
    :return: new text where the forbidden words are replaced with '*' according to their length
    """

    text = text.split()
    bad_words = [x.lower() for x in bad_words]
    punctuation = [".", "?", "!", ",", ";", ":", "[", "}", "{", "}", "(", ")", "'", '"']
    ellipsis_after_word = ["...", "***"]
    new_word = ""
    first_letter_boolean = False
    first_letter = ""
    for word in text:
        i = 1
        lower_word = word.lower()
        if lower_word[:1] in punctuation:
            first_letter = lower_word[:1]
            lower_word = lower_word[1:]
            first_letter_boolean = True
        while i <= len(word):
            if lower_word[:i] in bad_words:
                if lower_word[-3:] in ellipsis_after_word:
                    new_word = "*" * (len(word) - 3) + lower_word[-3:]
                elif first_letter_boolean and lower_word[-2:-1] in punctuation and lower_word[-1:] in punctuation:
                    new_word = first_letter + "*" * (len(word) - 3) + lower_word[-2:]
                elif first_letter_boolean in punctuation and lower_word[-1:] in punctuation:
                    new_word = first_letter + "*" * (len(word) - 2) + lower_word[-1:]
                elif first_letter_boolean in punctuation :
                    new_word = first_letter + "*" * (len(word) - 1)
                elif lower_word[-1:] in punctuation:
                    new_word = "*" * (len(word) - 1) + lower_word[-1:]
                else:
                    new_word = "*" * len(word)
                indexes = (a for a, value in enumerate(text) if value == word)
                for index_to_replace in indexes:
                    text[index_to_replace] = new_word
            i = i + 1
    text = " ".join(text)
    return text


