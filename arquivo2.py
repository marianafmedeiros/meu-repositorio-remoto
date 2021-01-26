from typing import List

def concat_words(word_list: List[str]):
    concat = ' '.join(word_list)
    return concat

def capitalize_first_letter(word_list: List[str]):
    final_list = []
    for word in word_list:
        capitalized = word.capitalize()
        final_list.append(capitalized)
    return final_list