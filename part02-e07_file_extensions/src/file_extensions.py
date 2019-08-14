#!/usr/bin/env python3

def file_extensions(filename):
    with open(filename, 'r') as f:
        no_ext = []
        ext_dict = {}
        for i in f:
            i = i.rstrip()
            if not '.' in i:
                no_ext.append(i)
            else:
                splitted = i.split('.')
                filename = splitted[0]
                extension = splitted[-1]
                try:
                    ext_dict[extension].append(i)
                except KeyError:
                    ext_dict[extension] = [i]

    return (no_ext, ext_dict)

def main():
    no_ext, ext_dict = file_extensions('src/filenames.txt')
    print(f'{len(no_ext)} files with no extension')
    for key, value in ext_dict.items():
        print(f'{key} {len(value)}')
        

if __name__ == "__main__":
    main()
