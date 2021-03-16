#!/usr/bin/env python3

def merge(L1, L2):
    i, j = 0, 0
    size1 = len(L1)
    size2 = len(L2)
    list = []

    while i < size1 and j < size2:
        if L1[i] < L2[j]:
            list.append(L1[i])
            i += 1
        else:
            list.append(L2[j])
            j += 1
    
    list += L1[i:] + L2[j:]

    return list

def main():
    L1 = [1, 2, 3, 4, 5, 6, 7, 8]
    L2 = [3, 6, 8, 10, 12, 13]
    print(merge(L1, L2))

if __name__ == "__main__":
    main()
