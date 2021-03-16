#!/usr/bin/env python3

def reverse_dictionary(d):
    result = {}
    for i in d.keys():
        for j in d[i]:
            if j not in result.keys():
                result[j] = [i]
            else:
                result[j].append(i)
    return result

def main():
    d={"move":["liikuttaa"], "hide":["piilottaa", "salata"], "six":["kuusi"], "fir": ["kuusi"]}
    reverse_dictionary(d)

if __name__ == "__main__":
    main()
