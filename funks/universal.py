import time


def slow_text(text, _time=0.03):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(_time)


def caesar_cipher(word):
    encrypted_word = ""
    for letter in word:
        if letter.isalpha():
            ascii_code = ord(letter)
            shifted_ascii_code = (ascii_code - ord('а') + 3) % 32 + ord('а')
            encrypted_word += chr(shifted_ascii_code)
        else:
            encrypted_word += letter
    return encrypted_word