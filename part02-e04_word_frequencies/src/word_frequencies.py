#!/usr/bin/env python3

def word_frequencies(filename):
    wordlist = []
    cnt_dictio = {}
    with open(filename, 'r') as f:
        for line in f:
            splitted = line.split()
            stripped = [i.strip("""!"#$%&'()*,-./:;?@[]_""") for i in splitted]
            for i in stripped:
                wordlist.append(i)
    wordset = set(wordlist)
    for i in wordset:
        cnt = wordlist.count(i)
        cnt_dictio[i] = cnt

    return cnt_dictio


def main():
    pass

if __name__ == "__main__":
    main()
