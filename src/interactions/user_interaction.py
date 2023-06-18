class UserInteraction:
    """
    @purpose
    This class has supportive functionality for user interaction-based methods.

    @methods:
        - get_text -
        - get_filename -
    """

    @staticmethod
    def get_text() -> str:
        return input("Type text you want to encrypt: ")

    @staticmethod
    def get_filename() -> str:
        return input("Type filename to decrypt: ")

    @staticmethod
    def get_rottype() -> str:
        return input("Choose your ROT type: ")

    @staticmethod
    def print_decoded(text: str) -> None:
        print(f"Your decoded text is: {text}")

    @staticmethod
    def show_buffer(buffer: dict) -> None:
        print(f"Your current state of buffer is: {buffer}")
