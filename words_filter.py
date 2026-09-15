VOWELS = set("аеєиіїоуюяaeiouy") #set для швидшого пошуку

def is_valid_word(word): # функція перевіряє чи слово відповідає вимогам (довжина > 5, починається на голосну)
    return len(word) > 5 and word[0].lower() in VOWELS


def filter_words(words): # функція приймає список слів і повертає новий відфільтрований список
    return [word for word in words if is_valid_word(word)]


words = ["apple", "jet", "avionics", "пайтон", "алгоритм", "конус"]

print(*filter_words(words), sep="\n") # функція виводить відфільтровані слова
    