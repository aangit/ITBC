
from image import ImageFile
from text_file import TextFile
from video_file import VideoFile

if __name__ == "__main__":
    text_file = TextFile("my_file", 1024, "Hi", "text")

    print(text_file.number_of_characters())
    print(text_file.get_last_modification_time())
    text_file.write_in_file("this is new content")
    print(text_file.number_of_characters())
    print(text_file.get_last_modification_time())
    print(text_file)
    image = ImageFile("photo", 2048, "beautiful photo",
                      "censuredcontentcensuredcontentcensuredcontentcensuredcontent123456789")
    print(image)
    print(image.get_image_size())
    video = VideoFile("movie", 4096, "check this out", "movie content")
    print(video)
    print(video.get_image_size())
    print(video.get_duration())
