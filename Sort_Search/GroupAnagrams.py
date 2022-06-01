#!/usr/bin/python3

##################
#
# This script groups all anagrams together in an array of strings
#
##################

def SortStr(item):
    item = list(item)
    helper = item.copy()
    MergeSort(item, helper, 0, len(item)-1)
    return "".join(item)

def MergeSort(item, helper, low, high):
    if low < high:
        midpt = low + (high - low) // 2
        MergeSort(item, helper, low, midpt)
        MergeSort(item, helper, midpt+1, high)
        Merge(item, helper, low, midpt, high)

def Merge(item, helper, low, midpt, high):
    for i in range(low, high+1):
        helper[i] = item[i]
    helpleft = low
    helpright = midpt + 1
    curr = low

    while helpleft <= midpt and helpright <= high:
        if helper[helpleft] <= helper[helpright]:
            item[curr] = helper[helpleft]
            helpleft += 1
        else:
            item[curr] = helper[helpright]
            helpright += 1
        curr += 1
    remain = midpt - helpleft
    for i in range(0, remain+1):
        item[curr+i] = helper[helpleft+i]

def GroupAnagram(arr):
    table = {}
    for item in arr:
        key = SortStr(item)
        if key in table:
            table[key].append(item)
        else:
            table[key] = [item]
    return Rearrange(arr, table)

def Rearrange(arr, table):
    i = 0
    while i < len(arr):
        for key in table:
            for item in table[key]:
                arr[i] = item
                i += 1
    return arr

##################

arr = ["abc", "adc", "cba", "ebkga", "ba", "akbge"]

#print(SortStr("aecdb"))
print(GroupAnagram(arr))
