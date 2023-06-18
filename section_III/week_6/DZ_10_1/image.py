from file import File


class ImageFile(File):
    def __init__(self, name: str, size: int, description: str, content: str):
        super().__init__(name, "img", size, description,  content)

    def get_image_size(self):
        return f"{len(self.content)} x {len(self.content)} "

