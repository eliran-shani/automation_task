# Sort and get max word occurrence

#### PreRequisites
1. Python3 ([Python/MAC] / [Python/Windows])

[Python/MAC]: https://realpython.com/installing-python/#macos-mac-os-x
[Python/Windows]: https://realpython.com/installing-python/#windows

#### Setup
1. Clone repo parseTextPython <br> 
    `git clone https://github.com/eliran-shani/automation_task.git`
2. Install requirements.txt <br>
    `pip3 install -r requirements.txt`

#### Usage

- Get help: <br>
	`./run.bash help`

- Run application using the following command: <br>
    `./run.bash [delimiter] [sort]`

	- **[delimiter]**: <br>
    **c** - comma separated <br>
    **s** - space seperated <br>
    **n** - newline seperated <br>

	- **[sort]**: <br>
    **a** - ascending <br>
    **d** - descending <br>

* Run application using **comma delimiter** and sort ascending / descending<br>
    `./run.bash c a` (ascending) <br>
    `./run.bash c d` (descending)<br>

* Run application using **space delimiter** and sort ascending / descending<br>
    `./run.bash s a` (ascending) <br>
    `./run.bash s d` (descending) <br>

* Run application using **newline delimiter** and sort ascending / descending<br>
    `./run.bash n a` (ascending) <br>
    `./run.bash n d` (descending) <br>

#### Functions

- **get_root_path** - Returns the root path
- **which_delimiter** - Returns the correspondent delimiter character
- **trim_irrelevant_characters** - Trims irrelevant characters
- **remove_duplicates** - Removes duplicates from the list
- **set_input_files** - Set all relevant input text files to parse
- **parse_text_from_file** - Parse a single text file into a single list of words
- **parse_all_files** - Parse all text files into one list of words
- **count_words** - Returns the number of occurrences per word
- **sort_text** - Sort words within an list
- **get_max_occurrence_word** - Returns an object with the max occurrence word
- **print_max_word** - Prints the max occurrence word
- **write_results_to_file** - Writes results into an output text file

#### Folder structure

    .
    ├── common                              # All commonly used functions / variables
        ├── helpers                         # Common functions
    ├── input                               # All input text files
        ├── c                               # Comma separated input text files
        ├── n                               # Newline separated input text files
        ├── s                               # Space separated input text files
    ├── output                              # All output results text files
    ├── tests                               # All related tests
    ├── .gitignore                          # Github ignore file
    ├── conftest                            # Pytest configuration file
    ├── requirements.txt                    # Python packages required to run this project 
    ├── run.bash                            # Script to run the application                          
    └── README.md

