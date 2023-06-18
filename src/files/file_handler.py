import json
import os
from datetime import datetime


class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def _save_rot13(self, content: list):
        output = {"type": "ROT13", "content": content, "timestamp": datetime.now().strftime("%Y-%m-%d")}
        json_object = json.dumps(output, indent=4)
        filename = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        save_path = os.path.join(os.getcwd(), "content", "rot13", f"{filename}.json")
        with open(save_path, "w") as outfile:
            outfile.write(json_object)

    def _save_rot47(self, content: list):
        output = {"type": "ROT47", "content": content, "timestamp": datetime.now().strftime("%Y-%m-%d")}
        json_object = json.dumps(output, indent=4)
        filename = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        save_path = os.path.join(os.getcwd(), "content", "rot47", f"{filename}.json")

        with open(save_path, "w") as outfile:
            outfile.write(json_object)

    def save(self, content: dict):
        rot13_content = content["rot13"]
        rot47_content = content["rot47"]

        self._save_rot13(rot13_content)
        self._save_rot47(rot47_content)

    def read(self, rot_type: str, filename: str):
        read_path = os.path.join(os.getcwd(), "content", rot_type, f"{filename}.json")

        with open(read_path, "r") as outfile:
            read_content = json.loads(outfile.read())

        return read_content
