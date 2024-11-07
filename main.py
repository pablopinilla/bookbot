def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_chars(text)
    sorted_list = chars_dict_to_sorted_list(chars)
    get_report(book_path, num_words, sorted_list)


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_chars(text):
    alphabet = {}

    lowered_text = text.lower()
    chars = list(lowered_text)
    for char in chars:
        if char in alphabet:
            alphabet[char] += 1
        else: 
            alphabet[char] = 1
    return alphabet

def get_report(path, num_words, sorted_list):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        else: 
            print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
