from cipherforge.banner import show_banner
from cipherforge.caesar import (
    encrypt as caesar_encrypt,
    decrypt as caesar_decrypt,
    brute_force
)
from cipherforge.vigenere import (
    encrypt as vigenere_encrypt,
    decrypt as vigenere_decrypt
)
from cipherforge.utils import (
    get_integer,
    get_non_empty_text,
    pause
)
from cipherforge import __version__


def clear_screen():
    print("\n" * 3)


def show_menu():

    print("""
╔══════════════════════════════════════════════════════════╗
║                    CIPHERFORGE MENU                     ║
╠══════════════════════════════════════════════════════════╣
║  [1] Caesar Cipher                                      ║
║  [2] Vigenère Cipher                                    ║
║  [3] Caesar Brute-Force Analysis                        ║
║  [4] About CipherForge                                  ║
║  [5] Help                                               ║
║  [0] Exit                                               ║
╚══════════════════════════════════════════════════════════╝
""")


def caesar_menu():

    clear_screen()

    print("""
╔══════════════════════════════════════════════════════════╗
║                    CAESAR CIPHER                        ║
╚══════════════════════════════════════════════════════════╝
""")

    text = get_non_empty_text("Enter text: ")
    shift = get_integer("Enter shift key: ")

    encrypted = caesar_encrypt(text, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    print("\n" + "─" * 55)
    print(f"Original Text  : {text}")
    print(f"Encrypted Text : {encrypted}")
    print(f"Decrypted Text : {decrypted}")
    print("─" * 55)

    pause()


def vigenere_menu():

    clear_screen()

    print("""
╔══════════════════════════════════════════════════════════╗
║                   VIGENÈRE CIPHER                       ║
╚══════════════════════════════════════════════════════════╝
""")

    text = get_non_empty_text("Enter text: ")
    key = get_non_empty_text("Enter key: ")

    try:

        encrypted = vigenere_encrypt(text, key)
        decrypted = vigenere_decrypt(encrypted, key)

        print("\n" + "─" * 55)
        print(f"Original Text  : {text}")
        print(f"Encrypted Text : {encrypted}")
        print(f"Decrypted Text : {decrypted}")
        print("─" * 55)

    except ValueError as error:

        print(f"\n[!] Error: {error}")

    pause()


def brute_force_menu():

    clear_screen()

    print("""
╔══════════════════════════════════════════════════════════╗
║              CAESAR BRUTE-FORCE ANALYSIS                 ║
╚══════════════════════════════════════════════════════════╝
""")

    ciphertext = get_non_empty_text("Enter ciphertext: ")

    print("\nPossible decryptions:\n")

    results = brute_force(ciphertext)

    for result in results:

        print(
            f"Shift {result['shift']:2} │ "
            f"{result['text']}"
        )

    pause()


def show_about():

    clear_screen()

    print("""
╔══════════════════════════════════════════════════════════╗
║                   ABOUT CIPHERFORGE                     ║
╚══════════════════════════════════════════════════════════╝

CipherForge is an educational cryptography toolkit.

Purpose:
    Explore classical encryption, decryption, and cipher analysis.

Current Algorithms:
    • Caesar Cipher
    • Vigenère Cipher

Project:
    DecodeLabs Cybersecurity Project 2

Developer:
    Muhammad Zubair

Version:
    """ + __version__)

    pause()


def show_help():

    clear_screen()

    print("""
╔══════════════════════════════════════════════════════════╗
║                     CIPHERFORGE HELP                    ║
╚══════════════════════════════════════════════════════════╝

Caesar Cipher:
    Encrypts or decrypts text using a numerical shift key.

Vigenère Cipher:
    Uses a repeating alphabetic key to perform polyalphabetic
    substitution.

Brute-Force Analysis:
    Attempts all 26 possible Caesar Cipher shifts.

Important:
    These classical ciphers are educational and are not secure
    for protecting real-world sensitive information.
""")

    pause()


def run():

    while True:

        clear_screen()
        show_banner()
        show_menu()

        choice = input("Select an option: ").strip()

        if choice == "1":
            caesar_menu()

        elif choice == "2":
            vigenere_menu()

        elif choice == "3":
            brute_force_menu()

        elif choice == "4":
            show_about()

        elif choice == "5":
            show_help()

        elif choice == "0":

            clear_screen()

            print("""
╔══════════════════════════════════════════════════════════╗
║              Thank you for using CipherForge             ║
╚══════════════════════════════════════════════════════════╝
""")

            break

        else:

            print("\n[!] Invalid option.")
            pause()
