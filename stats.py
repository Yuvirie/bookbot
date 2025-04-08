def count_words(text):
    word_list = text.split()
    return len(word_list)

def sort_on(dict):
    return dict["count"]

def count_chars(text):
    checked = set()
    result = {}
    text = text.lower()

    for letter in text:
        #check if letter was already checked and counted

        if letter in checked:
            continue
        else:
           splitted_text = text.split(letter)
           letter_num = len(splitted_text) - 1
           result[f"{letter}"] = letter_num
           checked.add(letter)
    
    return result


def report(data):
    
    #phase 1 -> new list
    result_list = []
    for item in data.items():
        letter, count = item
        if letter.isalpha():
            result_list.append({"char":letter, "count": count})

    #phase 2 -> sorting

    result_list.sort(reverse=True, key=sort_on)

    return result_list