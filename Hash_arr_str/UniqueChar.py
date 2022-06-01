#!/usr/bin/python3

####################
#
# This script determines whether a string has unique characters
#
####################

## Solution n.1 => O(NlogN) time, O(N) space

#def UniqueChar(string):
#    sorted_str = MergeSort(string)
#    for i in range(len(string)-1):
#        if sorted_str[i] == sorted_str[i+1]:
#            return False
#    return True

def MergeSort(string):
    if len(string) > 1:
        midpt = len(string)//2
        left_str = string[:midpt]
        right_str = string[midpt:]
    
        MergeSort(left_str)
        MergeSort(right_str)
        
        x, y, z = 0, 0, 0
        while x < len(left_str) and y < len(right_str):
            if left_str[x] < right_str[y]:
                string[z] = left_str[x]
                x += 1
            else:
                string[z] = right_str[y]
                y += 1
            z += 1
        
        while x < len(left_str):
            string[z] = left_str[x]
            x += 1
            z += 1

        while y < len(right_str):
            string[z] = right_str[y]
            y += 1
            z += 1

    return string

## Solution n.2 => O(N) time, O(N) space

#def UniqueChar(string):
#    CharTab = {}
#    for char in string:
#        if char in CharTab:
#            return False
#        else:
#            CharTab[char] = 1
#    return True

## Solution n.3 => O(N) time, O(1) space

def UniqueChar(string):
    checker = 0
    for char in string:
        val = ord(char) - ord("a")
        if checker & (1 << val) > 0:
            return False
        checker |= (1 << val)
    return True

####################

string = "absohuoer"
answer = False
print(UniqueChar(list(string)) == answer) 
