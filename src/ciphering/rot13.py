class Rot13:
    def execute(self, text):
        result = ""
        for v in text:
            c = ord(v)
            if ord("a") <= c <= ord("z"):
                if c > ord("m"):
                    c -= 13
                else:
                    c += 13
            elif ord("A") <= c <= ord("Z"):
                if c > ord("M"):
                    c -= 13
                else:
                    c += 13

            result += chr(c)

        return result
