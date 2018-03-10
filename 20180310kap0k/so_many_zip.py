#!/usr/bin/env python

import zipfile

zname = "flag.zip"

for i in range(1000):
    z = zipfile.ZipFile(zname, "r")
    z.extractall()
    zname = z.namelist()[0]
    z.close()
    if i % 100 == 0:
        raw_input("continue")
