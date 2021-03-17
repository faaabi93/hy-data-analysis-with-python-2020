#!/usr/bin/env python3

def extract_numbers(s):
    split = s.split()
    list = []
    for x in split:
        try:
            list.append(int(x))
        except:
            try: 
                list.append(float(x))
            except:
                pass

    return list

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
