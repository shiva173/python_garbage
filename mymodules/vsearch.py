def searchVowels(phrase: str) -> set:
    vowels = set('aieou')
    return vowels.intersection(set(phrase))
searchVowels('somephrase')


def searchLetters(phrase: str, letters: str='aeoui') -> set:  # аргументы и что возвращает
    # после_типа_можно_указать_значение_по_умолчанию
    return set(letters).intersection(set(phrase))

searchLetters(phrase='hello', letters='he')
