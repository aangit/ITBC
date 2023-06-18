import re
from main_book import *


if __name__ =="__main__":
    with open('20000 leagues-under-Jules-Verne-[ebooksread.com] copy.txt', 'r') as f:
        contents = f.read()

parts = re.split(r"PART", contents)
part_number = 1
for part in parts:
    fixed_part = "PART" + part
    chapters = re.split(r"CHAPTER", part)
    chapters.pop(0)

    for chapter in chapters:
        chapter_number = get_chapter_number(chapter)
        title = get_chapter_title(chapter)

        fixed_chapter = "CHAPTER"+chapter
        create_directory(part_number, chapter_number)

        with open(f"book/{part_number}/{chapter_number}/{title}.txt", "w") as f:
            f.write(fixed_chapter)

        analytics = count_occurencies(fix_invalid_characters(fixed_chapter))
        with open(f"book/{part_number}/{chapter_number}/Analytics_{chapter_number}.txt", "w") as f:
            f.write(str(analytics))

    create_all_analytics(part_number, chapters)
    part_number += 1