#!/usr/bin/env python3

def distinct_characters(L):
    res = {}
    for word in L:
        dist_chars = len(set(word))
        res[word] = dist_chars
    return res


def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
