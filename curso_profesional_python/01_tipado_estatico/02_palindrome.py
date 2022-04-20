def is_palindrome(string: str) -> bool:
    string = string.replace(' ', '').lower()

    return string == string[::-1]


if '__main__' == __name__:
    string = input('Enter a word: ')
    print(is_palindrome(string))
