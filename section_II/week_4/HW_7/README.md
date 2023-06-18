# Program 2: Book Analysis

This program reads a book file, `20000 leagues-under-Jules-Verne.txt`, consisting of CHAPTERs. It performs various analyses on each CHAPTER, including creating separate folders for each CHAPTER, extracting the text of each CHAPTER into separate files, and generating analytics files containing word frequency information for each CHAPTER.

Additionally, the program creates a folder named `all_analytics` and generates a file, `all_analytics.txt`, inside it. The `all_analytics.txt` file lists the CHAPTERs in descending order based on the number of words contained in each CHAPTER.

## Instructions

1. Ensure that the book file, `20000 leagues-under-Jules-Verne.txt`, is in the same directory as the program.
2. Run the program.
3. The program will create separate folders for each CHAPTER and extract the corresponding text into individual files.
4. It will also generate analytics files with word frequency information for each CHAPTER.
5. Finally, it will create the `all_analytics` folder and generate an `all_analytics.txt` file inside it, containing the word count for each CHAPTER in descending order.

### Bonus Task: Prefix Analysis

The program also performs an additional task of finding prefix lengths for each CHAPTER and writes them to separate files named `prefix_CHAPTER_chapternumber`.