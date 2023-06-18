import os
import re

from roman_numbers_converter import roman_to_int


def get_chapter_number(chapter_text: str) -> str:
    chapter_lines = chapter_text.splitlines()
    first_line = chapter_lines[0]
    match = re.findall(r'^\s*[IVXLCDM]+', first_line)[0]
    chapter_number = roman_to_int(match)
    return f"CHAPTER_{chapter_number}"


def get_chapter_title(chapter_text: str) -> str:
    for line in chapter_text.splitlines()[1:]:
        if line:
            return line.replace("\"", "").replace("/", "")


def count_occurencies(text: str) -> dict:
    word_count = {}
    count = 0
    for word in text.split():
        if word:
            word = word.lower()
            count += 1
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
    for key in word_count:
        word_count[key] = round(word_count[key] * 100 / count, 2)

    return word_count


def fix_invalid_characters(text: str) -> str:
    new_text = ""
    for i in text.splitlines():
        new_text += i.strip()
    separate = new_text.split('-')
    combined = ''.join(separate)
    return combined.replace(",", "").replace(".", "")


def create_directory(part_num: str, name: str) -> None:
    try:
        os.makedirs(f"book/{part_num}/{name}", exist_ok=True)
    except Exception as e:
        print(f"Error occured {e}")


def create_all_analytics(part_number: str, chapters: str) -> None:
    all_analytics = {}
    for chapter in chapters:
        fixed_chapter = "CHAPTER"+chapter
        word_count = len(fix_invalid_characters(fixed_chapter).split())
        all_analytics[get_chapter_number(chapter)] = word_count

    all_analytics_sorted = sorted(
        all_analytics.items(), key=lambda x: x[1], reverse=True)

    create_directory(part_number, "all_analytics")
    analytics_data = [f"{k}:{v}\n" for k, v in all_analytics_sorted]
    try:
        with open(f"book/{part_number}/all_analytics/all_analytics.txt", "w") as f:
            f.writelines(analytics_data)

    except Exception as e:
        print(f"Error uploading values {e}")