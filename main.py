#!/usr/bin/python3

import sys


def get_input(filename):
    input = open(filename, "r")
    lines = input.read().splitlines()
    return lines


def count_words(lines):
    count = 0
    for line in lines:
        words = line.split()
        for word in words:
            count += 1
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document ")
    print("")


def count_letters(lines):
    ordered_keys = []
    alphabet = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
                "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
                "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
                "y": 0, "z": 0}

    for line in lines:
        for letter in line.lower():
            if letter in alphabet:
                alphabet[letter] = alphabet.get(letter) + 1

    ordered_values = list(alphabet.values())
    ordered_values.sort()

    for order in ordered_values:
        ordered_keys.append(list(alphabet.keys())[list(alphabet.values()).index(order)])

    for i in range(25, -1, -1):
        print(f"The {ordered_keys[i]} character was found {ordered_values[i]} times")
    print("--- End report ---")


def main(filename):
    lines = get_input(filename)
    count_words(lines)
    count_letters(lines)


if __name__ == "__main__":
    main(sys.argv[1])
