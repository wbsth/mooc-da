#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    test = re.findall('\[\s*([\+\-]?\d+)\s*\]', s)
    return [int(i) for i in test]

def main():
    pass

if __name__ == "__main__":
    main()
