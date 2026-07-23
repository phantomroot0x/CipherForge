def _shift_character(character, shift):
    """
    Shift a single alphabetic character while preserving its case.
    Non-alphabetic characters remain unchanged.
    """

    if not character.isalpha():
        return character

    if character.isupper():
        base = ord("A")
    else:
        base = ord("a")

    return chr((ord(character) - base + shift) % 26 + base)


def encrypt(text, shift):
    """
    Encrypt text using the Caesar Cipher.
    """

    return "".join(
        _shift_character(character, shift)
        for character in text
    )


def decrypt(text, shift):
    """
    Decrypt text using the Caesar Cipher.
    """

    return encrypt(text, -shift)


def brute_force(ciphertext):
    """
    Try all 26 possible Caesar Cipher shifts.
    """

    results = []

    for shift in range(26):
        decrypted_text = decrypt(ciphertext, shift)

        results.append({
            "shift": shift,
            "text": decrypted_text
        })

    return results
