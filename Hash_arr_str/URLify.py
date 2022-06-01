#!/usr/bin/python3

###################
#
# This script replaces all spaces in a string with "%20"
# Assume sufficient space at the end and the true length is known
#
###################

def URLify(string, length, replace):
    string = list(string)
    replace = list(replace)

    space_count = 0
    for i in range(0, length):
        if  string[i] == " ":
            space_count += 1
    
    extra_len = space_count * ( len(replace)-1 )
    end_idx = length + extra_len - 1

    for i in range(length-1, -1, -1):
        if string[i] == " ":
            for j in range(len(replace)-1, -1, -1):
                string[end_idx] = replace[j]
                end_idx -= 1
        else:
            string[end_idx] = string[i]
            end_idx -= 1

    string = "".join(string)
    return string

###################

string = "Mr John Smith        "
length = 13
replace = "%20"

print(URLify(string, length, replace))
        
