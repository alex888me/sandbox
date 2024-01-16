import string
from typing import Dict


class Vigener:
    len_all_uppercase: int = len(string.ascii_uppercase)
    uppercase_index: Dict[str, int] = {letter: index for index, letter in enumerate(string.ascii_uppercase)}
    index_uppercase: Dict[int, str] = {index: letter for index, letter in enumerate(string.ascii_uppercase)}

    def __init__(self, key: str):
        self.key: str = key.upper()
        self.cursor: int = -1
        self.cursor_len: int = len(self.key) - 1

    def get_next_key_letter(self):
        if self.cursor == self.cursor_len:
            self.cursor = 0
        else:
            self.cursor += 1

        return self.key[self.cursor]

    def get_encrypted_letter(self, letter: str) -> str:
        next_key_letter = self.get_next_key_letter()
        index = self.uppercase_index[next_key_letter]
        encrypted_index = index + self.uppercase_index[letter]
        if encrypted_index >= self.len_all_uppercase:
            encrypted_index -= self.len_all_uppercase

        return self.index_uppercase[encrypted_index]

    def get_encrypted_letter(self, letter: str) -> str:
        next_key_letter = self.get_next_key_letter()
        index = self.uppercase_index[next_key_letter]
        encrypted_index = index + self.uppercase_index[letter]
        if encrypted_index >= self.len_all_uppercase:
            encrypted_index -= self.len_all_uppercase

        return self.index_uppercase[encrypted_index]

    def get_decrypted_letter(self, letter: str) -> str:
        next_key_letter = self.get_next_key_letter()
        index = self.uppercase_index[next_key_letter]
        decrypted_index = self.uppercase_index[letter] - index
        if decrypted_index < 0:
            decrypted_index = self.len_all_uppercase + decrypted_index

        return self.index_uppercase[decrypted_index]

    def encrypt(self, text: str) -> str:
        self.cursor = -1
        encrypted = []
        text = text.upper()
        for letter in text:
            encrypted.append(self.get_encrypted_letter(letter))

        return ''.join(encrypted)

    def decrypt(self, encrypted_text: str) -> str:
        self.cursor = -1
        decrypted = []
        encrypted_text = encrypted_text.upper()
        for letter in encrypted_text:
            decrypted.append(self.get_decrypted_letter(letter))

        return ''.join(decrypted)


cipher = Vigener('Lemon')
print(cipher.encrypt('AttackAtDown'))
print(cipher.decrypt('LXFOPVEFRBHR'))
