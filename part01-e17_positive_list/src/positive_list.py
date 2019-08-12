#!/usr/bin/env python3

def positive_list(L):
    def is_positive(number):
        return number > 0

    return(list(filter(is_positive, L)))


def main():
    pass

if __name__ == "__main__":
    main()
