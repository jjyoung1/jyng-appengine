from handler import Handler

class Rot13Handler(Handler):
    def get(self):
        text = "Please enter some text here"
        self.render("rot13.html", text=text)

    def post(self):
        text = self.request.get("text")
        text = self.encode(text)
        self.render("rot13.html", text=text)

    def encode(self, text):
        obfr = ""
        for char in text:
            # Only convert alpha characters
            if char.isalpha():
                # Determine base for wrap-around management
                if char.islower():
                    base = ord('a')
                else:
                    base = ord('A')

                # Convert the character
                c = ord(char) - base
                c += 13
                c = c%26 + base
                char = chr(c)
            obfr+=char
        return obfr
