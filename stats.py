# stats.py

def get_book_text(path):
    with open(path, 'r') as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def text_strings(text):
    char_text = text.lower()
    char_counts = {}

    for char in char_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_strings(char_counts):
    sorted_list = []

    for char, count in char_counts.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})

    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list