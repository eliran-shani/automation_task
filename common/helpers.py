import operator
import os
from os import listdir
from os.path import isfile, join


def get_root_path() -> str:
    relative_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(relative_path)


def which_delimiter(delimiter: str) -> str:
    """

    :param delimiter: the delimiter string value (c / s / n)
    :return:  The relevant delimiter character (c => "," / s => " " / n => "\n"
    """
    if delimiter == 'c':
        return ','

    if delimiter == 's':
        return ' '

    if delimiter == 'n':
        return '\n'


def trim_irrelevant_characters(text: list, delimiter: str) -> list:
    """

    :param text: a list of words
    :param delimiter: the delimiter character value ("," / " " / "\n")
    :return: a list of words stripped from irrelevant characters
    """
    new_text = []

    for word in text:
        if delimiter == ',':
            word = word.replace('\n', '')
            word = word.replace(' ', '')

        if delimiter == ' ':
            word = word.replace('\n', '')
            word = word.replace(',', '')

        new_text.append(word)

    return new_text


def count_words(words: list) -> list:
    """

    :param words: a list of words and occurrence
    :return: a sorted dictionary of words alone
    """
    counts = dict()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return sorted(counts.items(), key=operator.itemgetter(1), reverse=True)


def parse_text_from_file(file_name: str, delimiter: str) -> list:
    """

    :param file_name: The file name (text1.txt)
    :param delimiter: delimiter: the delimiter character value ("," / " " / "\n")
    :return: a list of words parsed from a text file
    """
    parsed_text = []

    input_folder_path = "{root}/input/{delimiter}".format(root=get_root_path(), delimiter=delimiter)

    with open("{path}/{file_name}".format(path=input_folder_path, delimiter=delimiter, file_name=file_name)) as file:
        delimiter = which_delimiter(delimiter)

        for line in file:

            if delimiter == '\n':
                for word in line.splitlines():
                    parsed_text.append(word.lower())

            if delimiter == ',' or delimiter == ' ':
                for word in line.split(delimiter):
                    parsed_text.append(word.lower())

                parsed_text = trim_irrelevant_characters(parsed_text, delimiter)

        return parsed_text


def parse_all_files(files: list, delimiter: str) -> list:
    temp_array = []

    for txt_file in files:
        temp_array.extend(parse_text_from_file(file_name=txt_file, delimiter=delimiter))

    return temp_array


def sort_text(sort_by: str, words: list) -> list:
    unique_sorted_list = []

    if sort_by == 'a':
        unique_sorted_list = sorted(remove_duplicates(words))
    elif sort_by == 'd':
        unique_sorted_list = sorted(remove_duplicates(words), reverse=True)

    return unique_sorted_list


def get_max_occurrence_word(words: list) -> object:
    """

    :param words: a list of words
    :return: an object with the word value and occurrence (e.g. (test),(6))
    """

    counted_words = count_words(words)

    class MaxWord(object):
        def __init__(self, word, occurrence):
            self.word = word
            self.occurrence = occurrence

    return MaxWord(word=counted_words[0][0], occurrence=counted_words[0][1])


def remove_duplicates(array: list) -> list:
    """

    :param array:  a list of words
    :return: a list without duplicates
    """
    return list(dict.fromkeys(array))


def write_results_to_file(array: list, name: str):
    """

    :param array: a list of words
    :param name: the output file name after the underscore "_"
    """

    output_folder_path = "{}/output/".format(get_root_path())
    output_file_path = os.path.join(output_folder_path, 'output_{name}.txt'.format(name=name))
    permissions = 0o755
    os.chmod(path=output_folder_path, mode=permissions)

    with open(output_file_path, 'w') as output_file:
        for word in array:
            output_file.write(word)
            output_file.write("\n")


def set_input_files(delimiter_type: str) -> list:
    """

    :param delimiter_type: the delimiter string value (c / s / n)
    :return: a list of existing input files
    """
    input_path = "{root}/input/{delimiter}/".format(root=get_root_path(), delimiter=delimiter_type)
    return [f for f in listdir(input_path) if isfile(join(input_path, f))]


def print_max_word(words: list):
    """

    :param words: a list of words
    """
    max_word_object = get_max_occurrence_word(words)
    print("\n\n'{word}' is the most frequent word, occurred {occurrence} times"
          .format(word=max_word_object.word, occurrence=max_word_object.occurrence))
