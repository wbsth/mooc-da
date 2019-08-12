#!/usr/bin/env python3

def find_matching(L, pattern):
    res = []
    for cnt, val in enumerate(L):
        if pattern in val:
            res.append(cnt)

    return res


def main():
    pass

if __name__ == "__main__":
    main()
