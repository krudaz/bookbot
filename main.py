#!/usr/bin/python3

import sys


def get_input(filename):
    input = open(filename, "r")
    lines = input.read().splitlines()
    return lines


def print_book(lines):
    for line in lines:
        print(line)


def count_words(lines):
    count = 0
    for line in lines:
        words = line.split()
        for word in words:
            count += 1
    print(f"Total Words = {count}")


def count_letters(lines):
    alphabet = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
                "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
                "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
                "y": 0, "z": 0}
    for line in lines:
        for letter in line.lower():
            if letter in alphabet:
                alphabet[letter] = alphabet.get(letter) + 1
    print(alphabet)


def main(filename):
    lines = get_input(filename)
    print_book(lines)
    count_words(lines)
    count_letters(lines)


if __name__ == "__main__":
    main(sys.argv[1])
