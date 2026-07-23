def get_integer(prompt):
    """
    Safely receive an integer from the user.
    """

    while True:

        try:
            return int(input(prompt))

        except ValueError:
            print("\n[!] Invalid input. Please enter a valid integer.\n")


def get_non_empty_text(prompt):
    """
    Receive non-empty text from the user.
    """

    while True:

        text = input(prompt)

        if text.strip():
            return text

        print("\n[!] Input cannot be empty.\n")


def pause():
    input("\nPress Enter to continue...")
