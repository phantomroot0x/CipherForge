def _validate_key(key):
    if not key:
        raise ValueError("Key cannot be empty.")

    if not key.isalpha():
        raise ValueError("Key must contain alphabetic characters only.")


def encrypt(text, key):
    """
    Encrypt text using the Vigenère Cipher.
    """

    _validate_key(key)

    result = []
    key = key.upper()
    key_index = 0

    for character in text:

        if character.isalpha():

            shift = ord(key[key_index % len(key)]) - ord("A")

            if character.isupper():
                base = ord("A")
            else:
                base = ord("a")

            encrypted_character = chr(
                (ord(character) - base + shift) % 26 + base
            )

            result.append(encrypted_character)
            key_index += 1

        else:
            result.append(character)

    return "".join(result)


def decrypt(text, key):
    """
    Decrypt text using the Vigenère Cipher.
    """

    _validate_key(key)

    result = []
    key = key.upper()
    key_index = 0

    for character in text:

        if character.isalpha():

            shift = ord(key[key_index % len(key)]) - ord("A")

            if character.isupper():
                base = ord("A")
            else:
                base = ord("a")

            decrypted_character = chr(
                (ord(character) - base - shift) % 26 + base
            )

            result.append(decrypted_character)
            key_index += 1

        else:
            result.append(character)

    return "".join(result)
