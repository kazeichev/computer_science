def WordSearch(length, string, search):
    words_list = generate_search_handbook(
        split_string(string.split(" "), length),
        length
    )

    return find_substring(words_list, search)


def split_string(strings, length):
    words_list = list()

    for word in strings:
        if len(word) > length:
            words_list.append(word[0:length])
            words_list += split_string([word[length:]], length)
        else:
            words_list.append(word)

    return words_list


def generate_search_handbook(strings, length):
    words_list = list()

    for word in strings:
        if len(words_list) == 0:
            words_list.append(word)
        else:
            last_string = words_list[-1]
            if (len(word) + len(last_string)) + 1 <= length:
                words_list[words_list.index(last_string)] = last_string + " " + word
            else:
                words_list.append(word)

    return words_list


def find_substring(strings, search):
    result = list()

    for string in strings:
        if search in string.split(" "):
            result.append(1)
        else:
            result.append(0)

    return result
