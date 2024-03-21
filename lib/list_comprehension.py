#!/usr/bin/env python3

def return_evens(num_List):
   evened = [n for n in num_List if n % 2 == 0]
   return(evened)

def make_exclamation(sentence_list):
    exclamationed = [n + "!" for n in sentence_list]
    return(exclamationed)