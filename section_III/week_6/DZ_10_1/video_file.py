from file import File

class VideoFile(File):
    def __init__(self, name: str, size: int, description: str, content: str):
        super().__init__(name, "mp4", size, description, content)
    
    def get_image_size(self):
        return f"{len(self.content)} x {len(self.content)} "

    def get_duration(self):
        return f"{len(self.content)*2} seconds"

