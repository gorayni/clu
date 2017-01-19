#!/bin/bash

# Recursively formats all xml files from the input directory
function format_xml {
    xml_dirpath=`realpath "$1"`
    echo $xml_dirpath
    for xml_filename in `find "$xml_dirpath" -name "*.xml" | sort`; do
        # Continue if file is empty
        if [ ! -s "$xml_filename" ]
        then
            continue
        fi
    	echo "$xml_filename"
    	original_file_permissions=`stat -c "%a" "$xml_filename"`
        cat $xml_filename | xmllint --format - > aux.xml
        mv aux.xml "$xml_filename"
        chmod "$original_file_permissions" "$xml_filename"
    done
}

function contains() {
    string="$1"
    substring="$2"
    if test "${string#*$substring}" != "$string"
    then
        return 1    # $substring is in $string
    fi
    return 0    # $substring is not in $string
}


function pad_zeros() {
    num_digits="$1"
    number="$2"
    printf %0"$num_digits"d $number
}