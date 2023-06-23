#!/bin/bash
# get the line number from where a function is called

get_line_number() {
    echo "This is line number: ${BASH_LINENO[0]}"
}

get_line_number