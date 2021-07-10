#!/usr/bin/env python3
import sys
from collections import OrderedDict

if len(sys.argv) != 2:
   sys.stderr.write(">>> Script requires a file argument")
   sys.exit(1)

for arg in sys.argv[1:]:
    lines = OrderedDict()
    with open(sys.argv[1]) as fd:
        for line in fd:
            tmp = line.strip()
            if tmp in lines.keys():
                lines[tmp] = lines[tmp] + 1
            else:
                lines[tmp] = 1

    for line,count in lines.items():
        if count == 1:
            print(line)