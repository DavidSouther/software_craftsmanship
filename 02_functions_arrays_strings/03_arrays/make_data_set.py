#!/usr/bin/env python3

"""
Adapted from Think Stats 2e, using the CFC NSFG.

https://www.cdc.gov/nchs/nsfg/index.htm

Pulls the dataset and extracts [prglngth, prgordr]
"""

import nsfg

df = nsfg.ReadFemPreg()

print("\"\"\"2002 NSFG values for [prgordr, prglngth]\"\"\"")
print("PREGNANCIES = [")
for index, frame in df.iterrows():
    if frame.outcome > 1:
        continue
    print("    [%d, %d]," % (frame.pregordr, frame.prglngth))
print("]")
