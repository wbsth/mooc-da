#!/usr/bin/env python3

def detect_ranges(L):
    # sorting the list
    sorted_list = sorted(L)

    seq_start = 0
    seq_end = 0

    result_list = []

    # iterating from 2nd to last element
    for i in range(1, len(sorted_list)):
        if sorted_list[i] - 1 == sorted_list[i-1]:
            seq_end = i
            # in case of last element
            if i == len(sorted_list)-1:
                result_list.append((sorted_list[seq_start], sorted_list[seq_end]+1))
                
        else:
            # seq ended, need to write to final list
            if seq_start == seq_end:
                # one-element sequence
                result_list.append(sorted_list[seq_start])
            else:
                result_list.append((sorted_list[seq_start], sorted_list[seq_end]+1))
                # multiple element sequence
            # write new seq start and end
            seq_start = seq_end = i
            
            # in case of last element
            if i == len(sorted_list)-1:
                result_list.append(sorted_list[-1])
    
    return result_list

def main():
    L = [-32, -51, -19, 80, -41, 23, 87, -72, 25, 27]
    result = detect_ranges(L)
    print(sorted(L))
    print(result)

if __name__ == "__main__":
    main()