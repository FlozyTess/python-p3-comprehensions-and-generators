#!/usr/bin/env python3

def return_evens(num_list):
    """Returns a list of all even numbers from the input list."""
    return [num for num in num_list if num % 2 == 0]
    pass

def make_exclamation(sentence_list):
    """Returns a list of sentences with an exclamation mark at the end."""
    return [sentence + "!" for sentence in sentence_list]
    pass