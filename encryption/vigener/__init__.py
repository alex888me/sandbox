import string

dictionary = string.ascii_uppercase

class Vigener:
    def __init__(self, key: str):
        self.key = key.upper()

    def encrypt(self, plain_text):
        current = 0
        encrypted = ''

        for letter in plain_text.upper():
            # print(letter, self.key[current], dictionary.index(letter), dictionary.index(self.key[current]))

            index = (dictionary.index(letter) + dictionary.index(self.key[current])) % len(dictionary)
            encrypted = encrypted + dictionary[index]

            if current >= len(self.key) - 1:
                current = 0
            else:
                current += 1
        return encrypted


    def decrypt(self, plain_text):
        current = 0
        decrypted = ''

        for letter in plain_text.upper():
            # print(letter, self.key[current], dictionary.index(letter), dictionary.index(self.key[current]))

            index = (abs(dictionary.index(letter)) - abs(dictionary.index(self.key[current]))) % len(dictionary)
            decrypted = decrypted + dictionary[index]

            if current >= len(self.key) - 1:
                current = 0
            else:
                current += 1
        return decrypted