import datetime

class File:

    def __init__(self, name : str, file_type:str, size: int, description: str, content: str):
        self.name = name
        self.file_type = file_type
        self.size = size
        self.description = description
        self.content = content
        self.__last_modification_time = File.get_current_time()

    def get_last_modification_time(self):
        return self.__last_modification_time


    @classmethod
    def get_current_time(cls):
        return str(datetime.datetime.now())

    def read_file(self):
        return self.content

    def write_in_file(self, new_content):
        self.content = new_content
        self.__last_modification_time = File.get_current_time()

    def __str__(self):
        return f"Name: {self.name}.{self.file_type}\nDescription:{self.description}\n{self.content}\nLast modification date: {self.get_last_modification_time()}"