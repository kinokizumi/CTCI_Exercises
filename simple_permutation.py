#!/usr/bin/python3

def permutation(string):
    permute(string, "")

def permute(string, prefix):
    if len(string)==0:
        print(prefix)
    else:
        for i in range(0, len(string)):
            rem = string[0:i] + string[i+1:]
            print('str= ', string, 'i= ', i, 'prefix= ', prefix)
            permute(rem, prefix+string[i])

permutation("abc")
