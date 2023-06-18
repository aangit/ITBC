from file import File


class TextFile(File):
    def __init__(self, name: str, size: int, description: str, content: str):
        super().__init__(name, 'txt', size, description, content)

    def number_of_characters(self):
        return len(self.content)
