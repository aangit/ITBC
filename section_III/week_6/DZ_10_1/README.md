# File System Interface

This project implements a simple file system interface, modeling files without directories. The file system supports different file types, including text files, image files, and video files. Each file has common attributes such as name, type, size, description, moment of last modification, and content.

## File Types

### Text Files (.txt)

- Additional Attribute: Character count
- Methods:
  - `read()`: Retrieves the content of the text file.
  - `write(content)`: Updates the content of the text file and modifies the moment of last modification.

### Image Files (.img)

- Additional Attribute: Image dimensions
- Methods:
  - `read()`: Retrieves the content of the image file.
  - `write(content)`: Updates the content of the image file and modifies the moment of last modification.

### Video Files (.mp4)

- Additional Attributes: Image dimensions, duration
- Methods:
  - `read()`: Retrieves the content of the video file.
  - `write(content)`: Updates the content of the video file and modifies the moment of last modification.

## Usage

In the `main` function, the following actions are performed:

1. Create an instance of a text file (`example.txt`) and call its methods (`read()` and `write()`).
2. Create an instance of an image file (`example.img`) and call its methods (`read()` and `write()`).
3. Create an instance of a video file (`example.mp4`) and call its methods (`read()` and `write()`).