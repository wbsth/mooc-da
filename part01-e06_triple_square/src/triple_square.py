#!/usr/bin/env python3

def triple(number):
    return number * 3

def square(number):
    return number ** 2

def main():
    for i in range(1, 11):
        tripled = triple(i)
        squared = square(i)
        if squared > tripled:
            break
        else:
            print(f"triple({i})=={tripled} square({i})=={squared}")
        

if __name__ == "__main__":
    main()
