def rythm_exists(text: str) -> bool:
    set_of_vowels = set('ауоиэыяюеё')
    text_strings = text.lower().split()
    count_vowels_list = [
        sum([1 for elem in string if elem in set_of_vowels])
        for string in text_strings
]
print(count_vowels_list)
return len(set(count_vowels_list)) == 1

def main() -> None:
    # input_string = input('Введите строку стихотворения: ')
    input_string = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
    if rythm_exists(input_string):
        print("Парам пам-пам")
    else:
        print("Пам парам")


if __name__ == '__main__':
    main()