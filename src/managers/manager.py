from buffers.buffer import Buffer
from ciphering.rot13 import Rot13
from ciphering.rot47 import Rot47
from config.context_options import CONTEXT_OPTIONS
from files.file_handler import FileHandler
from interactions.user_interaction import UserInteraction
from menus.context_menu import ContextMenu


class Manager:
    """
    @purpose
    This class is a facade which allows to control the flow of the application.

    @methods:
        - start - is for starting the application
        - execute - is for running specific option got from user
        - _encrypt_47 -
        - ...
    """

    def __init__(self) -> None:
        self._is_running = True

        self.context_menu = ContextMenu(CONTEXT_OPTIONS)
        self.rot47 = Rot47()
        self.rot13 = Rot13()
        self.buffer = Buffer()
        self.file_handler = FileHandler("content/encryption.json")

        self._options = {
            1: self._encrypt_47,
            2: self._encrypt_13,
            3: self._decrypt,
            4: self._save,
            5: self._peek_buffer,
            6: self._exit,
        }

    def _encrypt_47(self) -> None:
        text = UserInteraction.get_text()
        encrypted_text = self.rot47.execute(text)
        self.buffer.insert("Rot47", encrypted_text)

    def _encrypt_13(self) -> None:
        text = UserInteraction.get_text()
        encrypted_text = self.rot13.execute(text)
        self.buffer.insert("Rot13", encrypted_text)

    def _decrypt(self) -> None:
        rot_type = UserInteraction.get_rottype()
        filename = UserInteraction.get_filename()
        read_content = self.file_handler.read(rot_type, filename)

        encrypted_text = " ".join(read_content["content"])
        if rot_type == "rot13":
            decoded_text = self.rot13.execute(encrypted_text)
        elif rot_type == "rot47":
            decoded_text = self.rot47.execute(encrypted_text)

        UserInteraction.print_decoded(decoded_text)

    def _save(self) -> None:
        self.file_handler.save(self.buffer.storage)
        self.buffer.clear()

    def _peek_buffer(self) -> None:
        UserInteraction.show_buffer(self.buffer.storage)

    def _execute(self, choice: int) -> None:
        self._options.get(choice)()

    def _exit(self) -> None:
        self._is_running = False

    def start(self) -> None:
        while self._is_running is True:
            self.context_menu.display()
            choice = self.context_menu.get_choice()

            self._execute(choice)
