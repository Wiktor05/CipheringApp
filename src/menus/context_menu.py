class ContextMenu:
    def __init__(self, options: dict) -> None:
        self.options = options

    def display(self):
        print("Type number from menu below: ")
        for nr, value in self.options.items():
            print(f"{nr}. {value}")

    def get_choice(self):
        return int(input("Choose one option: "))
