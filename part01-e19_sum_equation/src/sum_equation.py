#!/usr/bin/env python3

def sum_equation(L):
    if len(L) == 0:
        return('0 = 0')
    else:
        numb_sum = sum(L)
        L_strings = [str(i) for i in L]
        return (' + '.join(L_strings) + ' = ' + str(numb_sum))

def main():
    print(sum_equation([]))

if __name__ == "__main__":
    main()
