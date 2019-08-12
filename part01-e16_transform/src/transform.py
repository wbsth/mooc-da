#!/usr/bin/env python3

def transform(s1, s2):
    result = []
    s1 = s1.split()
    s2 = s2.split()
    list1 = list(map(int, s1))
    list2 = list(map(int, s2))

    zipped = zip(list1, list2)
    for i in list(zipped):
        result.append(i[0] * i[1])

    return(result)

def main():
    transform("1 5 3", "2 6 -1")

if __name__ == "__main__":
    main()
