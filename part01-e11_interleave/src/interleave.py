#!/usr/bin/env python3

def interleave(*lists):
    lst = []
    lst2 = []
    for i in lists:
        lst.append(i)
    zipped = list(zip(*lst))
    for i in zipped:
        for j in i:
            lst2.append(j)
    return lst2
    

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
