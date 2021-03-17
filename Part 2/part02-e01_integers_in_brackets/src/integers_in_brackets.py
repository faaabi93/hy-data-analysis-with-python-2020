#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    #print(re.findall(r"\[\s*([+-]?\d+)\s*\]", s))
    list = re.findall(r"\[\s*([+-]?\d+)\s*\]", s)
    return [int(i) for i in list]

def main():
    integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx")

if __name__ == "__main__":
    main()
