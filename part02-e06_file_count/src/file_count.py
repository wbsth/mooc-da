#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename, 'r') as f:
        line_count, words_count, chars_count = 0, 0, 0

        for line in f:
            line_count += 1
            chars_count += len(line)
            words = line.split()
            words_count += len(words)
        
        return(line_count, words_count, chars_count)

def main():
    file_list = sys.argv[1:]
    
    for i in file_list:
        lines, words, chars = file_count(i)
        print(f'{lines}\t{words}\t{chars}\t{i}')

if __name__ == "__main__":
    main()
