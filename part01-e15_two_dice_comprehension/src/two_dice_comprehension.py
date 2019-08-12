#!/usr/bin/env python3

def main():
    res = [(x,y) for x in range(1,7) for y in range(1,7) if x+y == 5]
    for i in res:
        print(i)

if __name__ == "__main__":
    main()
