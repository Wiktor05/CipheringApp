class Rot47:
    def execute(self, text):
        x = []
        for i in range(len(text)):
            j = ord(text[i])
            if j >= 33 and j <= 126:
                x.append(chr(33 + ((j + 14) % 94)))
            else:
                x.append(text[i])
        return "".join(x)
