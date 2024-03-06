#!/usr/bin/env python3

# def filter_text(text):
#     # Your solution.
#     return True

def filter_text(text):
    rules = {}
    
    for line in text.split("\n"):
        if line.startswith("#"):
            key, val = map(str.strip, line[1:].split("="))
            rules[key] = val

    for key in rules.keys():
        if any(key in val for val in rules.values()):
            return False

    return True
