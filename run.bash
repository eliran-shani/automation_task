#!/usr/bin/env bash

if [[ $1 = "help" ]]; then
   echo -e " \n" \
        " >>> Guide <<< \n" \
        " (*) Run program using the following syntax:" \
        " $ ./run.bash [Delimiter] [Sort] \n \n" \
        " >>> Examples <<< \n" \
        " (*) Run program using comma delimiter and sort by ascending:" \
        " $ ./run.bash c a \n" \
        " (*) Run program using space delimiter and sort by descending:" \
        " $ ./run.bash s d \n" \
        " (*) Run program using newline delimiter and sort by ascending:" \
        " $ ./run.bash n a \n \n" \
        " >>> Options <<< \n" \
        " (*) Delimiter options: \n" \
        "     c - (comma) \n" \
        "     s - (space) \n" \
        "     n - (new line) \n" \
        " (*) Sort by options: \n"  \
        "     a - (ascending) \n" \
        "     d - (descending) \n \n" \
        " >>> Input <<< \n" \
        " (*) Comma delimiter input files:" \
        " ./input/c/*.txt \n" \
        " (*) Space delimiter input files:" \
        " ./input/s/*.txt \n" \
        " (*) Newline delimiter input files:" \
        " ./input/n/*.txt \n \n" \
        " >>> Output <<< \n" \
        " (*) Comma delimiter output files:" \
        " ./output/output_c.txt \n" \
        " (*) Space delimiter output files:" \
        " ./output/output_s.txt \n" \
        " (*) Newline delimiter output files:" \
        " ./output/output_n.txt \n"
else
   python3 -m pytest -s --delimiter $1 --sort $2
fi