#!/usr/bin/env python3

def extract_numbers(s):
    ret_list = []
    splitted = s.split()
    for word in splitted:
        try:
            ret_list.append(int(word))
        except:
            try:
                ret_list.append(float(word))
            except:
                pass

    return ret_list

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
