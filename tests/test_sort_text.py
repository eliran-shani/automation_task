from common.helpers import set_input_files, \
    write_results_to_file, parse_all_files, sort_text, print_max_word


def test_run(delimiter, sort):
    # Set relevant input text files by delimiter type
    input_files = set_input_files(delimiter)

    # Parse text from all input files
    all_words = parse_all_files(files=input_files, delimiter=delimiter)

    # Sort by Ascending / Descending
    unique_sorted_list = sort_text(sort_by=sort, words=all_words)

    # Write results to relevant output file
    write_results_to_file(unique_sorted_list, name=delimiter)

    # Print the most frequent word and its occurrence
    print_max_word(words=all_words)
