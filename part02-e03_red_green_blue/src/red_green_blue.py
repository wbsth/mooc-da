#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    res_list = []
    regexpr = r'(\d+)\s+(\d+)\s+(\d+)\s+(.+)'
    with open(filename, 'r') as f:
        next(f)
        for i in f:
            res_list.append('\t'.join(re.search(regexpr, i).groups()))
    return res_list


def main():
    pass

if __name__ == "__main__":
    main()
