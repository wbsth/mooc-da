#!/usr/bin/env python3

class Prepend(object):
    def __init__(self, s):
        self.s = s

    def write(self, text):
        print(f'{self.s}{text}')
        

def main():
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()
